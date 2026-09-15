<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0137.txt",
      "sha256": "81636e5a8c3cb4b47701e497cac31bd4c67bda3e84e3ac610e08434c4d22a7c6",
      "bytes": 15337
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d2c3029a8c625c76b4d4a72c7c61a87ccb8faa3aabc4e67459b775ede20e42f0",
      "bytes": 1809
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c42516e1a67d986632bea2354fdb25ef42b8dd6d5cb89da651bfde256fdbab9e",
      "bytes": 27681
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "94fd972a3c6ffdae981dc3771bbc5084eaa81bd3492859b21ae678bd1eaca816",
      "bytes": 755
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e25069bc634cec94c068d765e342e04f6584ba0d33546ca5a7c76a72713c70b8",
      "bytes": 5353
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a119e82232855ca3696e4bf38f756de047b3ba57b7ea83b2303c746afa7d4ad3",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ff70f4b9371319bf28d25071618a89f1949f0bf52f714ee3caa5b918ee22991a",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "5c92dff78810e254886a5e62ee27655b2f5466cafa9597808897af7271623695",
      "bytes": 630
    },
    {
      "path": "characters/Woo Jintae.md",
      "sha256": "f7b4c3c6c6237ff514f42ab01ad35707a2b2e93fe071ed85821b380f514312e4",
      "bytes": 805
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "6bf9662969d450a664ecccb810b06fbca473fe4e78f467988d69512df0f0fb63",
      "bytes": 22748
    }
  ],
  "estimated_tokens": 23598
}
-->

# Durable State Update — Chapter 137

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 137. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 137. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 137,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 137,
    "continuity_sources": [137],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "Woo Jintae is unconscious after Taekyung beats and verbally humiliates him for refusing to apologize.",
    "Taekyung orders the four remaining Five Gates heirs to receive ten sword-case blows each.",
    "The guests at Honghwa Inn recognize Taekyung as the Sleeping Dragon of Shanxi and publicly favor the Jin Family of Taiyuan over the Five Gates of Shanxi.",
    "Jang Childeuk is revealed to be the Level 15 public speaker defending the Jin Family of Taiyuan.",
    "Cheongpung asks to hit the final remaining heir because he has never done so before.",
    "The fall of the Mount Heng Sword Sect has shifted the balance of Shanxi Murim toward the Jin Family of Taiyuan.",
    "The current Five Gates heirs must attend Prince Shangshan's noon luncheon despite their injuries.",
    "Seok is the chief steward of Honghwa Inn.",
    "Cheongpung has never experienced a hot spring and joins Taekyung and Mujin after hearing about Honghwa Inn's hot springs.",
    "An unnamed Third-Rank Assistant Military Commissioner has reached eight-tenths mastery of the Seven Plum Sword and is summoned to the luncheon."
  ],
  "continuity_sources": [
    136
  ],
  "open_questions": [],
  "safe_through": 136,
  "temporary_decisions": [
    "Render 천지신명 as “Heaven and Earth and all the divine spirits.”",
    "Render 엎드려뻗쳐 as lying face down.",
    "Render 첫 경험 빌런 as “first-experience villain.”",
    "Render 칠매검 as “Seven Plum Sword.”",
    "Render 상산왕 as “Prince Shangshan.”",
    "Render 정 소협 and 갈 소협 as “Young Hero Jeong” and “Young Hero Gal.”",
    "Render 도지휘첨사 as “Assistant Military Commissioner.”",
    "Render 교권 향상 as “Improve teacher authority!”"
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 136
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 136
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 136
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 136
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 136
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family who summons martial officials and young Murim prodigies to a noon luncheon.
- **Personality:** His personal temperament is not established; his authority is treated as commanding and difficult to refuse.
- **Voice:** No direct speech appears in this chapter.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies.

### Woo Jintae.md

# Woo Jintae (우진태)

- **Safe through:** Chapter 136
- **Aliases:** None
- **Role:** Heir of the Seongun Escort Bureau and a leading scion of the current Five Gates of Shanxi; hosts its young members at Honghwa Inn and prepares for the City Lord's luncheon.
- **Personality:** Boastful, calculating, status-conscious, and manipulative; treats lavish gifts and money as tools for creating obligations, but becomes enraged and desperate when publicly humiliated.
- **Voice:** Charming and lavish in public, with polished courtesy that turns dry and contemptuous when he judges someone beneath him.
- **Relationships:** Heir to the Seongun Escort Bureau; cultivates the current Five Gates scions through hospitality, gifts, and bribes.

## Korean source

```text
＃137화



“기침하셨습니까?”

별채의 문을 열고 불쑥 들어온 낯익은 얼굴.

막 운기조식을 끝마친 나는 가부좌를 풀며 입을 열었다.

“대답도 안 했는데 들어오냐?”

“에이, 조장님과 제가 그 정도로 먼 사이는 아니잖습니까.”

“너랑 내가 어떤 사이인데?”

“피를 나누지는 않았지만 등을 맞댈 수 있는 전우? 애정과 신뢰로 똘똘 뭉친 군신(君臣) 관계?”

“애정? 음. 네가 아침부터 뒈지게 맞고 싶어서 작정을 했구나.”

“한 대 맞죠, 뭐. 설마 죽기야 하겠습니까.”

갈수록 능청스러움만 일취월장이다. 그냥 피식 웃으며 고개를 저었다.

“됐고, 새벽부터 웬일이야?”

“그야 당연히…… 잠깐, 저 양반 뭡니까? 여기서 잤어요?”

혁무진이 황당하다는 시선으로 구석에 널브러져 있는 청풍을 바라봤다.

“아니, 별채에 방이 몇 갠데 왜 여기서 자.”

“내버려 둬. 그럴 수도 있지. 측간 다녀와 보니 잠들어 있더라.”

결론부터 말하자면 청풍의 정체를 알아내는 것은 깔끔하게 실패했다.

그가 온천에서 나오자마자 노곤하게 잠이 들었기 때문이다. 깨우기도 뭣해서, 나도 그냥 잤다.

“아무리 그래도 그렇죠. 어제 처음 만난 외간 남자를 방에 들이시면 어떡합니까.”

“……말이 좀 묘하다?”

“그런 말이 아니고요. 좀 더 조심하란 말씀을 드리는 겁니다.”

“조심은 무슨. 누가 들으면 저 친구가 암살자라도 되는 줄 알겠다.”

“아니라는 법 있습니까?”

“뭐?”

“조장님은 다 좋은데, 무림을 너무 호락호락하게 보시는 것 같습니다. 무림이 얼마나 복잡한 은원으로 얽혀 있는 곳인데요. 방심하다간 정말 골로 갑니다.”

“재수 없는 소리 하네. 골로 보내 줘?”

“아, 진짜! 농담이 아니라니까요.”

답답하다는 듯 가슴을 퍽퍽 친 혁무진이 푹 잠들어 있는 청풍을 경계심 어린 눈빛으로 바라봤다.

“좀 이상하지 않습니까? 젊은 나이에 어울리지 않게 무공도 상당히 뛰어난 것 같은데 거지꼴로 돌아다니는 것만 봐도 그렇고. 그렇다고 개방의 제자도 아니잖아요.”

“원래 성격이 저렇게 돼먹은 거 아닐까.”

“저게 다 경계심을 누그러트리기 위한 위장이라면요? 훈련된 살수(殺手)라면 충분히 가능한 일 아닙니까?”

“살수라니? 날 노릴 사람이 어디 있다고.”

“왜 없습니까?”

“너도 알다시피 내가 어디서 원한을 품을 만큼 막돼먹은 놈은 아니잖아.”

“……어제만 따져도 원한 품을 사람이 다섯 명은 생긴 것 같은데요.”

듣고 보니 맞는 말이네.

하지만 청풍을 살수로 의심하는 건 너무 과민 반응이다.

나는 여전히 의구심 어린 시선으로 그를 흘끗대는 혁무진에게 말했다.

“이 친구는 아니야. 살수였다면 내가 지금까지 살아 있겠어?”

“뭐, 그건 맞죠.”

“그리고 살수는 무슨 놈의 살수. 산서오문인가 하는 놈들 빼면 나한테 원한 가질 일이 뭐가 있겠어?”

“대장로는 조장님께 무슨 개인적인 원한이 있어서 죽이려고 했겠습니까? 지난 전쟁에서 죽은 본가의 무인들은요?”

“그건…… 그렇지.”

혁무진이 고개를 절레절레 내저었다.

“저는 조심하라는 말씀을 드린 것뿐입니다. 무림의 은원은 굉장히 은밀하고 끈질겨서, 언제 어디서 무슨 일이 벌어질지 아무도 모르니까요.”

“으음.”

“먹음직스러운 음식에는 온갖 날벌레가 꼬이는 법. 산서잠룡이라는 이름이 널리 알려질수록 귀찮은 일들이 많아질 겁니다. 다짜고짜 생사결을 겨루자고 찾아오는 놈들도 있을 정도니까요.”

세상은 넓고 미친놈들은 많구나. 처음 들어 보는 이야기에 놀라는 한편 혁무진에게 감탄했다.

이 녀석, 오랜만에 상당히 도움 되는 말을 해 주는데.

“너 제법 아는 게 많다? 아주 기특해.”

“어흠. 뭐 이런 걸 갖고 그러십니까. 그냥 이것저것 많이 본 거죠.”

역시 현지인. 무림에서 내 나이쯤 되다 보면 살수가 사람 죽이는 것도 보고, 뭐 그러는 모양이다.

“원래 무림에서는 그런 일이 일상다반사로 일어나나? 저잣거리 나가면 무인들끼리 시비 붙어서 싸우고 있고. 뭐 그런 거야?”

“예?”

혁무진이 눈을 깜빡였다.

“무슨 말씀이십니까? 여기 태원이에요. 치안 엄청 좋아요.”

“아, 그럼 자주는 아니고 가끔?”

“가끔이라뇨? 제가 태원진가에 입문하기 전에 태원에서 이십 년 가까이 살았지만 무인들끼리 싸우는 건 한 번도 못 봤습니다.”

“……응?”

“서쪽으로 반 시진 거리에 성주가 머무는 산서성부(山西城府)가 있고 동쪽으로 한 시진이면 태원진가가 나옵니다. 괜히 칼부림 나 봤자 인생 피곤해져요. 밑바닥 낭인들도 인의대협 행세하는 곳이 태원인데. 모르셨어요?”

이 새끼가 지금 무슨 말을 하고 있는 걸까.

나는 잠깐의 침묵 끝에 입을 열었다.

“그, 이것저것 많이 봤다며?”

“뭘요? 아, 그거요?”

“그래, 그거.”

“그거야 당연히 책에서 읽은 거죠.”

“……책?”

“네. 집 앞에 나이 지긋하신 노인이 운영하는 서점이 있었거든요. 철전 한 냥에 반 시진씩 책을 읽을 수 있는 곳이었죠. 거기서 제 꿈을 키웠습니다.”

혁무진이 추억에 잠긴 눈빛으로 창밖을 응시했다.

“점소이 검신 되다, 아파야 무인이다, 무림의 아들 걸어서 구주팔황 세 바퀴 반 등등…… 참 재밌었습니다.”

“아, 그 책들을 읽고 무인이 되기로 마음먹었구나.”

“그럼요. 몇 권은 서점 망할 때 직접 사서 소장도 했습니다. 빌려드릴까요?”

“아냐, 됐어. 그나저나 무진아.”

“예?”

“너 진짜 맞아 뒈지고 싶니?”

감탄했던 내가 병신이지.

이 무협 소설 덕후 새끼가 하다 하다 소설과 현실을 혼동하는구나. 나는 혁무진의 멱살을 움켜잡았다.

“소설이랑 현실이랑 같아? 응? 네가 본 소설에 혓바닥 잘못 놀려서 맞아 죽은 놈은 안 나오던?”

“자, 잠깐! 잠깐만요! 제가 직접 그런 걸 목격한 건 아니지만 무림은 충분히…….”

“네, 다음 씹덕.”

빡!



* * *



홍화객잔은 태원의 중심부에 위치해 있다. 산서의 노른자위 땅이라 불리는 태원에서도 목 좋기로 유명한 곳.

그런 홍화객잔 앞이 사람들로 붐비는 것은 당연한 광경이었지만, 오늘은 유난히도 심했다.

“어이구, 이게 다 무슨 일이래?”

“마차에 군병에……. 이보게 양 씨, 뭐 들은 거 없어? 전쟁이라도 일어나나?”

“나도 몰러.”

웅성거림 속에서 여섯 마리의 준마가 끄는 호화롭고 거대한 마차가 우뚝 멈췄다.

이어 족히 일백에 달하는 군병이 오와 열을 맞춰 홍화객잔의 입구에 시립하자 관복을 차려입은 관리가 힘차게 외쳤다.

“상산왕 전하의 왕명(王命)을 받들라!”

“왕명을 받들라!”

왕명이라는 짧은 단어가 주는 막대한 무게감. 거기에 더해 일백의 정예병들 입에서 터져 나온 천둥 같은 외침에 한껏 숨죽인 목소리가 곳곳에서 흘러나왔다.

“자네 방금 들었나?”

“내 귀는 무슨 장식인 줄 알아? 왕명이라고 한 거 다 들었네.”

“무슨 일인지 감 좀 잡히는 것 없나?”

“듣기로는 홍화객잔에 산서잠룡이 묵고 있다 하던데, 아마 그것 때문이 아니겠나? 어린 전하께서 무공을 좋아하시는 거야 익히 알려진 사실이니까.”

“그거야 나도 알고 있네만…… 지금껏 이렇게까지 요란하게 한 적이 없으니까 하는 말이지.”

“뭐, 요즘 산서잠룡이 워낙 유명해지긴 했지. 얼마 전에는 관군을 대신해서 적풍단인가 하는 놈들도 쓸어 버렸으니 큰 공을 세우기도 했고.”

“혹시 벼슬이라도 내리실 생각…… 헛, 나온다. 나와!”

누군가의 외침에 수많은 시선이 객잔의 입구로 쏠렸다.

활짝 열린 문 앞, 내리쬐는 햇빛 아래 왕의 부름을 받은 당사자들이 모습을 드러내자 관중들 사이에서도 뜨거운 열기가 피어올랐다.

“오오, 저분이 산서잠룡인가?”

“한둘이 아닌데?”

“검을 찬 걸 보니 다른 후기지수들인가 보지, 뭐.”

“그래서 산서잠룡이 누구야?”

“딱 보면 모르겠나? 중간에 가장 크고 잘생긴 놈. 아니, 저분이 바로 산서잠룡 진태경 소협일세.”

“아따, 다들 선남선녀가 따로 없네, 그려.”

사람들의 수군거림처럼 모습을 드러낸 다섯 사람은 각기 용봉(龍鳳)이라 할 만했다.

그중 진태경의 존재감은 단연 군계일학. 중앙에 우뚝 선 그를 향해 경탄 어린 시선이 쏟아지던 그 순간이었다.

“으헉.”

털썩!

“……?”

“……?”

난데없이 후기지수 중 한 사람이 풀썩 쓰러지는 게 아닌가.

구경하던 사람들은 물론이고 시립해 있던 군병들까지 이게 뭔가, 하는 눈빛으로 쓰러진 후기지수를 바라봤다.

“커흠, 커허험!”

관리의 헛기침에 쓰러진 이의 얼굴이 새빨갛게 물들었다.

바닥에 엎어졌던 후기지수가 갓 태어난 송아지처럼 바들바들 떨리는 다리로 일어나자 관리가 붉은색 비단을 펼쳤다.

“커흠. 무림의 후기지수들은 왕명을 받들라! 이는 거룩한 천자의 아우인 과인이…….”

“꺅!”

털썩!

이번에 쓰러진 이는 여인이다.

예기치 못한 사고에 순간 관리의 숨이 거칠어졌다. 그러나 그는 왕명을 전달하는 몸. 고작 이런 일에 흐트러져서는 안 된다.

관리는 다시 한번 호흡을 가다듬었다.

“과, 과인이…….”

“허억!”

털썩!

“그, 그대들에게 내리는…….”

“히익!”

털썩!

이번에는 관리도 화를 피할 수 없었다. 혀를 깨물었는지 으득, 하는 소리와 함께 입가에서 피가 줄줄 흘러내린다.

아까와는 다른 의미로 침묵에 잠긴 좌중.

절망에 빠진 관리에게 당당한 걸음으로 다가온 한 사람이 속삭였다.

“저기, 굳이 밖에서 할 필요 있습니까? 그냥 안에서 하시죠?”

진태경의 말에 잠시 고민하던 관리가 대답했다.

“그헙시하.”

“……그냥 고개만 끄덕이세요. 옷에 피 튀어요.”



* * *



관리가 침통한 얼굴로 입을 열었다.

“도대체 이게 어떻게 된 일이오?”

다들 내 눈치만 살피고 있는 상황. 결국, 내가 간단명료하게 상황을 설명할 수밖에 없었다.

“애들이 좀 아픕니다.”

“아프다니, 그게 무슨?”

“파릇파릇한 무림의 동량들 아닙니까. 강해지려 너무 수련에 몰두한 나머지 몸이 안 좋아져서 픽픽 쓰러진 겁니다.”

“그게 정말이오?”

“…….”

“…….”

쥐 죽은 듯이 조용하다. 나는 슬쩍 돌아서며 물었다.

“정말이냐고 물으시는데, 혹시 못 들으셨습니까?”

산서오문의 후기지수 네 사람이 귀신을 본 것처럼 화들짝 놀란다.

“아, 아니오. 들었소. 잠시 대답을 생각하느라…….”

“마, 맞아요. 전 그냥 누가 대답할 줄 알고…….”

“생각할 게 뭐가 있나요. 그냥 사실대로 말하면 되는데. 안 그렇습니까? 허허허.”

물론 사실대로 말하면 나와의 일대일 면담 시간을 갖게 될 거다. 법은 멀고, 주먹은 가까운 법.

앞으로 산서 무림에서 멀쩡히 살아가려면 태원진가 눈치를 볼 수밖에 없는 네 사람은 억지로 입꼬리를 끌어당겼다.

“뭐, 일이 이렇게 된 겁니다.”

관리는 미심쩍다는 듯한 눈빛으로 재차 질문했다.

“한데 왜 한 사람은 안 보이는 거요? 내가 알기로 진 소협을 포함해서 여섯 사람이 되어야 맞는데.”

“아, 성운표국의 소국주 말씀이시군요.”

“그럴 거요. 이름이 아마…….”

“진태요. 우진태.”

“맞소. 그는 왜 자리에 나오지 않았소?”

그야 그 한 사람은 도저히 사람 꼴이 아니기 때문이지.

산서오문의 후기지수들이 이번 오찬에 나와 함께 초대된 놈들이란 걸 진작 알았다면 그 정도로 때리진 않았을 거다.

‘뭐, 엎질러진 물이니 어쩌겠어.’

최대한 수습하는 수밖에.

나는 최대한 안타까운 얼굴로 고개를 저었다.

“어젯밤, 사소한 시비가 붙어 부상을 당했는데 지금까지 정신을 차리지 못하고 있습니다.”

“시비? 주먹다짐이라도 했단 말이오?”

“비슷합니다. 어쨌든 얼굴 상태도 그렇고, 도저히 사람들 앞에 보이기 힘들 지경입니다.”

“허어어, 전하께서 초대한 객을 그 꼴로 만들다니. 어떤 천인공노할 놈이.”

“…….”

이거 기분 되게 묘하네. 범인을 코앞에 두고 역모죄라며 중얼거리던 관리가 한탄했다.

“큰일이오. 이유가 어찌 되었건 초대에 응하지 못하는 것은 사실. 이 사실을 아시면 전하께서 얼마나 진노하실지.”

“그, 제가 잘 말씀드려 보면 안 될까요?”

“공자가 몰라서 그렇지, 전하께서 한번 마음이 상하시면 아무도 말릴 수 없소. 당분간 인근이 쑥대밭이 될 거요.”

“쑥대밭이 되다뇨? 그건 또 무슨 말씀이십니까?”

“뭐겠소? 우선 성운표국의 소국주를 상하게 한 놈을 잡아들여 엄중히 문책할 것이고, 치안이 엉망인 이유를 들어 수십 명이 관직에서 물러날 거요. 그중에는 나도 있겠지.”

“…….”

아니, 왜 그렇게까지 해.

한창나이에 정리 해고를 당하게 생긴 관리는 처연한 표정으로 화룡점정을 찍었다.

“먹여 살려야 할 식구들이 열이 넘는데……. 휴우, 하늘이 원망스럽군.”

심지어 대가족이라니.

좌불안석이 된 내가 필사적으로 머리를 굴리던 그때였다.

“흐아아암.”

분위기에 안 맞는 태평한 하품. 기지개를 쭉 켜고 내려오는 한 사람을 보니 눈이 번쩍 뜨인다.

“저기, 이렇게 하는 건 어떻습니까?”

“응? 뭘 말이오?”

“더 대단한 후기지수를 데려가면 아무 문제 없는 거잖아요. 그렇죠?”

“확실하진 않지만 아마도 그럴 거요. 더 뛰어난 인물을 찾았다는데 뭐라 하시진 않을 테니.”

됐다. 나는 득의양양한 미소와 함께 청풍을 향해 손을 흔들었다.

무려 절정 고수씩이나 되는 후기지수다.

“혹시 황족 본 적 있어요?”
```

## Final English reading copy

```markdown
# Chapter 137

“Are you awake?”

A familiar face abruptly opened the annex door and barged in.

I had just finished circulating my qi, so I unfolded my legs from the lotus position and spoke.

“You came in without even waiting for an answer?”

“Come on, Captain. You and I aren’t that distant.”

“What kind of relationship do you and I have?”

“Not related by blood, but comrades who can fight back-to-back? A lord-and-vassal relationship tightly bound by affection and trust?”

“Affection? Hmm. You’ve made up your mind to get beaten half to death first thing in the morning.”

“One hit, then. Surely I won’t die.”

He was getting more shameless by the day. I let out a quiet laugh and shook my head.

“Enough. What brings you here so early?”

“Obviously… Wait, what’s with that guy? Did he sleep here?”

Hyuk Mujin stared incredulously at Cheongpung, who was sprawled out in the corner.

“Why would he sleep here when the annex has several rooms?”

“Leave him. These things happen. I found him asleep when I got back from the privy.”

To cut to the conclusion, I had failed completely at figuring out Cheongpung’s identity.

The moment he got out of the hot spring, he had fallen asleep from exhaustion. I couldn’t bring myself to wake him, so I slept, too.

“Even so, Captain. How could you let a strange man you met yesterday sleep in your room?”

“…That sounded a little strange.”

“That’s not what I meant. I’m saying you should be more careful.”

“Careful? Anyone listening to you would think he was an assassin.”

“Can you say for certain that he isn’t?”

“What?”

“You’re a good man in many ways, Captain, but I think you take the Murim too lightly. This is a place tangled up in complicated gratitude and grudges. If you let your guard down, you really could end up dead.”

“What an unlucky thing to say. Want me to send you there?”

“Seriously! I’m not joking.”

Mujin thumped his chest in frustration, then watched the sleeping Cheongpung with wary eyes.

“Isn’t he a little strange? He seems remarkably skilled for someone so young, yet he wanders around dressed like a beggar. And he isn’t even a Disciple of the Beggars’ Sect.”

“Maybe that’s just the way he’s wired.”

“What if all of that is just a disguise meant to lower people’s guard? If he were a trained assassin, it would be entirely possible.”

“An assassin? Who would even want to target me?”

“Why wouldn’t anyone?”

“You know I’m not such a bastard that I make people hold grudges against me everywhere I go.”

“…Just counting yesterday, I think at least five people now have a grudge against you.”

Come to think of it, he had a point.

But suspecting Cheongpung of being an assassin was an overreaction.

I spoke to Mujin, who was still shooting Cheongpung suspicious glances.

“This guy isn’t one. If he were an assassin, would I still be alive?”

“Well, that’s true.”

“And what assassin? Aside from those Five Gates of Shanxi bastards, who could possibly have a reason to hold a grudge against me?”

“Did the Head Elder try to kill you because of some personal grudge? What about the martial artists of our family who died in the last war?”

“That… is true.”

Mujin shook his head from side to side.

“I’m only telling you to be careful. The gratitude and grudges of the Murim run deep and stay hidden, so no one knows when or where something might happen.”

“Hmm.”

“Flies swarm around appetizing food. The more famous the name Sleeping Dragon of Shanxi becomes, the more trouble you’ll have to deal with. There are even people who show up out of nowhere and challenge you to a life-and-death duel.”

The world was a big place, and there were plenty of lunatics in it. I was surprised to hear something I had never imagined, but I was also impressed by Mujin.

*This guy is saying something genuinely useful for once.*

“You know quite a lot. What a good boy.”

“Ahem. It’s nothing worth making a fuss over. I’ve just seen a lot of things.”

As expected of a local. People in the Murim around my age had apparently seen assassins killing people and all kinds of other things.

“Does that sort of thing happen every day in the Murim? You know, you go out to the market and see martial artists getting into arguments and fighting each other?”

“What?”

Mujin blinked.

“What are you talking about? This is Taiyuan. The public order is excellent.”

“Oh. So not often, but sometimes?”

“Sometimes? I lived in Taiyuan for nearly twenty years before entering the Jin Family of Taiyuan, and I never once saw martial artists fighting each other.”

“…What?”

“The Shanxi Provincial Office, where the City Lord resides, is half a shichen west of here, and the Jin Family of Taiyuan is one shichen east. Starting a sword fight for no reason would only make your life miserable. Even the lowest wandering martial artists pretend to be Great Heroes of honor and justice in Taiyuan. You didn’t know that?”

What the hell was this guy talking about?

After a brief silence, I spoke.

“You said you’d seen a lot of things, didn’t you?”

“What? Oh, that?”

“Yes, that.”

“Of course I read about that in books.”

“…Books?”

“Yes. There was a bookstore run by an old man in front of my house. For one nyang in iron coins, you could read books for half a shichen. That’s where I nurtured my dreams.”

Mujin gazed out the window with a nostalgic look in his eyes.

*The Shop Assistant Becomes a Sword God, You Must Hurt to Become a Martial Artist, The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes,* and so on. They were really interesting.

“Oh, so you decided to become a martial artist after reading those books.”

“Of course. I even bought and kept a few of them when the bookstore went under. Would you like to borrow them?”

“No, I’m good. Anyway, Mujin.”

“Yes?”

“Do you really want to get beaten to death?”

I was an idiot for being impressed.

This wuxia-novel otaku bastard was confusing fiction with reality. I grabbed Mujin by the lapels.

“Do you think novels and reality are the same? Huh? Didn’t any of the novels you read have someone getting beaten to death for running his mouth?”

“W-wait! Wait! I’ve never personally witnessed anything like that, but the Murim is more than capable of—”

“Right, next otaku.”

*Smack!*

* * *

Honghwa Inn stood in the center of Taiyuan. Even in Taiyuan, which was known as Shanxi’s prime real estate, it was famous for its excellent location.

It was only natural for the area in front of Honghwa Inn to be crowded with people, but today the crowd was unusually large.

“Oh dear, what’s all this?”

“There’s a carriage and soldiers… Hey, Mr. Yang, have you heard anything? Is there a war breaking out?”

“I haven’t heard nothin’.”

Amid the murmuring, a luxurious, enormous carriage drawn by six fine horses came to a stop.

Then at least a hundred soldiers stood in neat ranks at the entrance to Honghwa Inn. An official dressed in his robes shouted loudly,

“Receive the royal command of His Highness Prince Shangshan!”

“Receive the royal command!”

The short phrase royal command carried tremendous weight. On top of that, the thunderous cry of a hundred elite soldiers caused hushed voices to spill out from every direction.

“Did you hear that?”

“Do you think my ears are decorations? I heard them say royal command.”

“Any idea what this is about?”

“I heard the Sleeping Dragon of Shanxi is staying at Honghwa Inn. Isn’t it probably because of him? Everyone knows the young Prince likes martial arts.”

“I know that much, but I’m saying this because he’s never made such a commotion before.”

“Well, the Sleeping Dragon of Shanxi has become awfully famous lately. He even wiped out those Red Wind Band bastards in place of the government troops not long ago, so he’s certainly done the Prince a great service.”

“Do you think His Highness plans to grant him an official post… Ah, they’re coming. They’re coming!”

At someone’s shout, countless eyes turned toward the entrance of the inn.

The doors stood wide open. As the people summoned by the Prince appeared beneath the glaring sunlight, a wave of excitement spread through the onlookers.

“Oh! Is that the Sleeping Dragon of Shanxi?”

“There’s more than one of them.”

“They’re wearing swords, so I suppose the others are young prodigies, too.”

“Then which one is the Sleeping Dragon of Shanxi?”

“Can’t you tell at a glance? The tallest and most handsome one in the middle. That’s Young Hero Jin Taekyung, the Sleeping Dragon of Shanxi.”

“My, my. They’re all handsome men and beautiful women, aren’t they?”

As the people whispered, five figures emerged, each one worthy of being called a dragon or phoenix.

Among them, Jin Taekyung’s presence was head and shoulders above the rest. At the very moment admiring gazes poured toward him as he stood tall in the center—

“Ugh!”

*Thud!*

“…?”

“…?”

One of the young prodigies suddenly crumpled to the ground.

Not only the onlookers but even the soldiers standing at attention stared at the fallen prodigy as though they had no idea what was going on.

“Ahem. Ahem!”

When the official cleared his throat, the fallen man’s face turned bright red.

The young prodigy who had fallen flat on his face got back up on legs trembling like a newborn calf. The official unfurled a red silk scroll.

“Ahem. The young prodigies of Murim shall receive the royal command! I, the younger brother of the holy Son of Heaven…”

“Eek!”

*Thud!*

This time, the one who collapsed was a woman.

The unexpected accident made the official’s breathing turn ragged for a moment. But he was the bearer of a royal command. He couldn’t let something so trivial throw him off.

The official composed himself and took another breath.

“I, I…”

“Gasp!”

*Thud!*

“The command I issue to you…”

“Eek!”

*Thud!*

This time, even the official couldn’t escape the disaster. Perhaps he had bitten his tongue, because a cracking sound came from his mouth, followed by blood streaming down his lips.

The crowd fell silent, though for a different reason than before.

As the official stood there in despair, one person approached him with a confident stride and whispered,

“Do we really have to do this outside? Why not just do it inside?”

The official considered Taekyung’s words for a moment before answering.

“Let’sh do that.”

“…Just nod. You’ll get blood on your clothes.”

* * *

The official spoke with a grave expression.

“How on earth did this happen?”

Everyone was watching me for a response. In the end, I had no choice but to explain the situation as briefly and clearly as possible.

“The kids aren’t feeling well.”

“Not feeling well? What do you mean?”

“They’re the fresh young pillars of Murim, aren’t they? They trained so hard to become stronger that they wore themselves down and keep collapsing.”

“Is that really what happened?”

“…”

“…”

It was quiet enough to hear a mouse breathe. I turned slightly and asked,

“He’s asking whether that’s true. Did you not hear him?”

The four young prodigies of the Five Gates of Shanxi jolted as though they had seen a ghost.

“O-oh, no. We heard him. We were just thinking of an answer…”

“Th-that’s right. I was waiting for someone else to answer…”

“What was there to think about? Just tell him the truth. Isn’t that right? Hahaha.”

Of course, if they told the truth, they would get some private one-on-one time with me. The law was far away, and fists were close at hand.

The four of them, who had no choice but to stay on the good side of the Jin Family of Taiyuan if they wanted to live in peace in Shanxi Murim, forced smiles onto their faces.

“Well, that’s what happened.”

The official looked suspicious and asked another question.

“But why is one person missing? As I understand it, there should be six people, including Young Hero Jin.”

“Ah, you mean the Young Bureau Head of the Seongun Escort Bureau.”

“That must be him. His name was…”

“Jintae. Woo Jintae.”

“That’s right. Why hasn’t he come out?”

*Because that one is in no condition to be seen as a human being.*

If I had known from the start that the Five Gates of Shanxi’s young prodigies had been invited to this luncheon with me, I wouldn’t have beaten him quite so badly.

*Well, what’s done is done.*

All I could do was clean up the mess as best I could.

I shook my head with the most sympathetic expression I could manage.

“Last night, he got injured after a minor disagreement and still hasn’t regained consciousness.”

“A disagreement? Are you saying he got into a fistfight?”

“Something like that. In any case, his face is in such a state that he simply can’t appear in front of people.”

“Good heavens. What kind of fiend would do that to a guest invited by His Highness?”

“…”

This felt really strange. With the culprit standing right in front of him, the official muttered something about treason, then lamented.

“This is a serious matter. Whatever the reason, the fact remains that he can’t attend the invitation. How furious will His Highness be when he learns of this?”

“Could I perhaps explain things to him properly?”

“Young Master, you don’t understand. Once His Highness takes offense, no one can stop him. The surrounding area will be turned into a wasteland for the time being.”

“Turned into a wasteland? What do you mean by that?”

“What else could I mean? First, they’ll arrest and severely punish the man who injured the Young Bureau Head of the Seongun Escort Bureau. Then, citing the terrible state of public order, dozens of officials will be forced to resign. I’ll probably be one of them.”

“…”

Why would they take it that far?

The official, who looked like he was about to be laid off in the prime of his life, added the finishing touch with a tragic expression.

“I have more than ten family members to feed… Sigh. I can only blame the heavens.”

*He has a big family, too.*

Just when I was unable to sit still and desperately racking my brain, it happened.

“Yaaawn.”

A carefree yawn completely out of place in the atmosphere.

My eyes lit up when I saw someone coming downstairs with a long stretch.

“Hey, how about we do this?”

“Hm? What do you mean?”

“If we bring along an even more impressive young prodigy, there won’t be a problem. Right?”

“I can’t be certain, but that’s probably true. His Highness wouldn’t complain if you found someone even more outstanding.”

Perfect.

With a triumphant smile, I waved at Cheongpung.

He was a young prodigy who was no less than a Peak master.

“Have you ever seen a member of the imperial family?”
```
