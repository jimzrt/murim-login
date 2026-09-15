<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0136.txt",
      "sha256": "f46e564749f4204c27bc7e8dce6d1fbf6dc9c796c3e0f7741ee0ad2833b8c930",
      "bytes": 13256
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1d64379189c31ccf39eeb574b728b918be088be7ff3be8ea9d504f4177f1d02d",
      "bytes": 926
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c84177b336ceb467ef1e867776bf1deeff25175fce5f6a0b398fb33bfa07b62d",
      "bytes": 26786
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "1d7a2c4dc1a204bd6dc3e760f650d9fd2972e150a8231101af11f2a0a5bf86b3",
      "bytes": 755
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "d10728bc507e5802d206ebe18b2a15bea03282977ff40fcd8ba8f8ce85398f7f",
      "bytes": 5353
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e4a618670edefd892069975c81b01f5d1a6a27e110d5abd181837114741d304b",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5c2573af6b4238cfd24c9b25b6de75288203ebf612ca83e6fe55147a6931399f",
      "bytes": 622
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "c92a54b7a37680815bd6bee744eaeba79bcf7b2a14661f040a7fa96d60b113c6",
      "bytes": 2374
    },
    {
      "path": "characters/Woo Jintae.md",
      "sha256": "6a1eee4b0e2854d9640852e7ce50edfc911f4cfd20a00e26fd93ce6449670bd9",
      "bytes": 805
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b81fcf0b3e6de424aabe9cf1789cea94522c7d9794ada0cb6f08a2c1ac7fe071",
      "bytes": 22414
    }
  ],
  "estimated_tokens": 22160
}
-->

# Durable State Update — Chapter 136

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 136. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 136. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 136,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 136,
    "continuity_sources": [136],
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
    "Cheongpung asks to hit the final remaining heir because he has never done so before."
  ],
  "continuity_sources": [
    135
  ],
  "open_questions": [],
  "safe_through": 135,
  "temporary_decisions": [
    "Render 천지신명 as “Heaven and Earth and all the divine spirits.”",
    "Render 엎드려뻗쳐 as lying face down.",
    "Render 첫 경험 빌런 as “first-experience villain.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 초식     | **form**                                         | Numbered technique movement                           |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 지부장    | **Branch Leader**                            |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 135
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 135
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 134
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 135
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 128
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

### Woo Jintae.md

# Woo Jintae (우진태)

- **Safe through:** Chapter 135
- **Aliases:** None
- **Role:** Heir of the Seongun Escort Bureau and a leading scion of the current Five Gates of Shanxi; hosts its young members at Honghwa Inn and prepares for the City Lord's luncheon.
- **Personality:** Boastful, calculating, status-conscious, and manipulative; treats lavish gifts and money as tools for creating obligations, but becomes enraged and desperate when publicly humiliated.
- **Voice:** Charming and lavish in public, with polished courtesy that turns dry and contemptuous when he judges someone beneath him.
- **Relationships:** Heir to the Seongun Escort Bureau; cultivates the current Five Gates scions through hospitality, gifts, and bribes.

## Korean source

```text
＃136화



“끄응.”

“으으으.”

신음을 흘리던 두 사람의 시선이 부딪쳤다. 엉덩이를 훤히 드러낸 채 엎드린 서로의 모습을 마주 보니 민망하면서도 묘한 동질감이 들었다.

“커흠. 정 소협, 상처는 어떠시오?”

“크흠. 뭐 그럭저럭. 갈 소협은?”

“난 죽을 것 같, 헉!”

“사실 본인도 마찬가지, 윽!”

말하다 보니 또 고통이 찾아왔다. 두 사람은 눈물을 찔끔 흘리며 중얼거렸다.

“재수가 없어도 정도가 있지. 하고 많은 사람 중에 하필이면 산서잠룡이라니.”

“그러게 말입니다. 살면서 이런 수모를 겪을 줄이야.”

분위기는 침울했다.

기라성 같은 문파들이 즐비한 중원(中原)이라면 모를까, 변방에 속하는 산서성에서는 두 사람 모두 침 좀 뱉고 방귀깨나 뀌는 문파의 후계자들이었다.

살면서 아쉬운 소리 한번 해 본 적 없었는데 지금은 흠씬 두들겨 맞고 침상에 누워 앓는 소리를 내고 있다.

“항산검문이 건재할 때만 하더라도 산서오문이 이 정도는 아니었는데…….”

“그때가 좋았지요.”

몇 달 전이라면 산서오문을 필두로 중소 문파 연합이 목소리를 낼 수 있었겠지만, 이제는 찍소리도 못 한다. 산서 무림의 균형이 깨진 것이다.

항산검문이 몰락한 이상, 산서 무림의 무게 추는 태원진가로 기울 수밖에 없다.

“아버지께서 아시면 절 죽이실 겁니다.”

“이하 동문이오. 그리 신신당부하셨는데 이런 일이 생긴 줄 아시면. 으으, 생각하기도 싫소.”

자그마치 백 명이 넘어가는 사람들 앞에서 그런 개망신을 당했으니. 곧 다가올 원단쯤에는 산서 전역에 소문이 퍼져 있을 것이 분명했다.

“마음 같아서는 멀리 도망치고 싶소.”

“도망이고 나발이고, 내일 걸을 수나 있을지 모르겠습니다. 그렇다고 성주의 부름을 거절할 수도 없고…….”

“다리가 부러져도 일단 가야지 어쩌겠소? 그냥 성주도 아니고 황족(皇族)인데.”

“그래야죠. 그나마 얼굴은 멀쩡해서 다행입니다.”

“그러게 말이오.”

두 사람의 시선이 자연스럽게 옆으로 옮겨 갔다.

죽은 듯이 누운 우진태의 얼굴은 말벌 떼에게 쏘인 것처럼 부풀어 있었다. 간혹 힘겹게 내쉬는 숨이 아니었다면 이미 죽었다고 생각했을 거다.

“아무리 그래도 그렇지, 사람을 어찌 저렇게 팰 수가 있답니까?”

“산서잠룡이 이 정도로 잔인한 놈일 줄은 몰랐소.”

“그나마 미리 머리를 박고 있어서 망정이지, 저희도 우 형님과 같은 꼴이 날 뻔했습니다.”

“충분히 그러고도 남지. 여인들도 가차 없이 두들겨 패는 놈 아니오?”

일행 중에는 여인이 둘이나 끼어 있었다. 사내라면 젊고 아름다운 여인들 앞에서 마음이 약해질 법도 한데, 진태경이라는 놈의 반응은 예상을 뛰어넘었다.



‘나이.’

‘네, 네?’

‘나이. 몇 살이냐고.’

‘여, 열일곱인데요.’

‘넌?’

‘저, 저는 열여덟이어요.’



열일곱, 열여덟. 꽃다운 나이다. 슬슬 혼사 이야기가 오고 가도 이상하지 않을 나이이기도 했다.

모두 진태경이 혹 여인들에게 관심이 있는 건가, 생각하던 그때였다.



‘엉덩이 더 높이 들어. 뼈 나간다.’

빡! 빡!

‘머리에 피도 안 마른 것들이! 벌써부터 술을 마시고!’

빡! 빡!

‘마실 거면 숨어서 곱게 마시든가! 가만히 있는 사람한테 시비를 걸고!’

빡! 빡!

‘인성이 덜 됐어! 너희 같은 것들 때문에 체벌이 필요한 거야! 알아, 몰라!’

빡! 빡!

‘교권 향상! 어느 정도의 체벌은 반드시 필요하다!’

빡! 빡! 빡!



방금의 일을 떠올린 두 사람이 몸을 부르르 떨었다.

한 명은 혼절했고, 다른 한 명은 사람들 앞에서 눈물 콧물을 쏙 뺐다.

그 많은 사람 앞에서 외간 남자에게 엉덩이를 흠씬 두들겨 맞았으니 혼삿길 막히는 건 시간문제일 거다.

“도대체 교권 향상이 무슨 말이오? 맹자에 나오는 말인가?”

“저도 모릅니다. 심지어 한 대 더 때리지 않았습니까.”

“악랄한 놈…….”

“그래도 저는 다른 분들이 부럽습니다.”

“아니, 그건 또 무슨 천인공노할 소리요? 지금 엉덩이에 피멍 잔뜩 든 거 안 보이시오?”

“다른 분들은 최소한 산서잠룡한테 맞지 않았습니까. 저는 웬 거지 같은 놈한테…… 크흑!”

“아, 저런.”

“차라리 산서잠룡한테 맞았으면 변명이라도 하지, 어디서 굴러먹다 왔는지 모르는 비루먹은 놈이 제 엉덩이를……. 무슨, 돈도 아니고 매질을 빌린답니까?”

치욕감에 턱이 파르르 떨렸다. 진태경에게 검갑을 양도받더니 신나게 후려치던 거지꼴의 사내가 생각나서다.



‘와, 이거 재밌네요! 엉덩이 탄력이 좋으신데요?’

빡! 빡! 빡!

‘아프세요? 얼마나 아프세요? 혹시 괜찮으시다면 더 세게 때려도 될까요? 제가 이런 경험은 처음이라 힘 조절이 미숙해도 이해해 주세요!’

빡! 빡! 빡!



죽기 직전까지, 아니 죽어서도 잊지 못할 치욕의 순간을 경험했다. 마음 같아서는 놈의 머리부터 발끝까지 잘근잘근 씹어 삼켜도 성치 않았다.

“그놈은 절대 용서할 수 없습니다!”

“걱정 마시오. 내 힘닿는 데까지 정 소협을 돕겠소!”

그들이 누군가, 산서오문의 후계자들이다. 태원진가의 진태경이라면 몰라도 젊은 거지 하나쯤은 충분히 처리할 수 있을 만한 힘을 가졌다.

“저기 그런데…….”

“예?”

“그놈, 확실히 거지 맞소? 겁이 나서 그러는 것이 아니라, 이번에 산서잠룡 일도 그렇고, 만전을 기해서 손해 볼 것 없다는 생각이 갑자기 드는데…….”

“……그럼 좀 더 알아볼까요?”

“그, 그럽시다.”

세상 물정 모르던 금수저들이 줄빠따를 맞고 경각심을 갖게 됐다.



* * *



교육이 마무리된 뒤 우리는 객실로 자리를 옮기기로 했다.

1층에 계속 머무르기엔 주위 손님들의 시선이 아무래도 신경 쓰였기 때문이다.

사람들의 주목에 어깨 으쓱하는 것도 한두 번 잠깐이지, 이런 상황에서 뭘 먹었다가는 음식이 입으로 들어가는지 코로 들어가는지도 헷갈릴 거다.

“홍화객잔을 책임지고 있는 석 모라고 합니다. 편하게 석 총관이라고 불러 주십시오.”

산서잠룡 이름값이 좋긴 좋다. 지금까지 털끝 하나 보이지 않던 총관이라는 자가 와서 고개를 숙일 정도면.

‘이 양반도 하오문 소속이겠지?’

홍화루는 하오문 산서 총지부장인 월화가 거점으로 삼은 곳이고, 홍화객잔은 이름에서 알 수 있듯이 그 하부 조직이나 다름없다.

어쩌면 이 사람은 내가 홍화객잔에 발을 들이기 전부터 나의 존재를 알고 있었을 것이다.

‘썩 유쾌한 기분은 아닌데.’

보이지 않는 시선들이 내 일거수일투족을 감시한다고 생각하는 건 좀 과민 반응인가?

하지만 그렇다고 마냥 불쾌하지는 않다.

그저 약간의 경계심이랄까. 지금까지는 확실히 우호적인 관계를 맺어 왔지만, 앞으로의 상황이 어떻게 될지는 아무도 모르는 거니까.

“따로 조용한 자리를 마련해 두었습니다.”

“오, 좋죠.”

알아서 서비스해 준다는데 거절할 이유가 없다. 총관을 따라 발걸음을 옮기려던 그때였다.

“지금까지 감사했습니다, 은인.”

목소리를 따라 고개를 돌리자 천진난만한 웃음을 머금고 있는 청풍이 보였다.

“그게 무슨 말이에요? 설마 이대로 가시려고?”

“네. 밤도 늦었으니 저는 이만 가 보려고요.”

가긴 어딜 가. 중간에 웬 잡것들이 끼어드는 바람에 대화도 제대로 못 했는데. 나는 황급히 손을 내저었다.

“에헤이, 밤이 늦었으면 하룻밤 묵고 가셔야지. 여비도 없다면서요?”

“괜찮아요. 노숙은 익숙해서요.”

“익숙하면 안 되죠. 그렇지, 새로운 경험! 객잔에서 자 본 적 있어요?”

“여비를 잃어버리기 전에 객잔에서 몇 번 묵었어요. 그리고 지금까지 두 분께 신세 진 것으로도 족합니다.”

옆에 있던 혁무진이 중얼거렸다.

“그렇긴 하지. 내 빙당호로…….”

“넌 조용히 하고. 그래서 정말 가시게요?”

“예. 다행히 아직 산서성에 볼일이 남았으니 기회가 된다면 다시 뵐 수 있을 거예요.”

이쯤 되니 할 말이 없다. 절정 고수가 제 발로 떠나겠다는데 밤길이 험하다고 붙잡을 수도 없는 것 아닌가.

다만 갑자기 튀어나온 이 별종의 정체가 아직도 궁금하기 짝이 없었다.

“혹시 갈 곳 없으면 태원진가로 오세요. 제 이름 대면 통과시켜 줄 테니까.”

“아, 그러고 보니 태원진가의 공자셨죠. 산서잠룡 진태경…… 은인의 이름을 기억해 두겠습니다.”

아까부터 내 신분을 알고 있었음에도 별 동요가 없다. 아, 그렇구나. 딱 이 정도 반응이다.

혁무진이 은근슬쩍 눈치를 주며 끼어들었다.

“태원진가. 모르시오?”

“글쎄요. 어디서 들어 본 것 같기도 하고. 귀에 익긴 한데 잘은 모르겠어요.”

잠시 갸웃거리던 청풍이 우리를 향해 고개를 숙였다.

“인연이 닿으면 다시 뵙겠지요. 그럼 이만.”

나는 진한 아쉬움을 담아 인사했다.

“조심히 가세요. 태원진가 꼭 잊지 마시고.”

“하하, 당연하죠.”

그가 시원한 웃음과 함께 돌아서자, 대화가 마무리됐다고 생각한 총관이 입을 열었다.

“그럼 별채로 모시겠습니다.”

“아, 네. 무진아, 가자.”

“오오, 그 유명하다는 홍화객잔의 별채에서 잘 수 있는 겁니까?”

“봉황객잔에서도 별채에 묵었는데 뭘 새삼스럽게.”

“무슨 소리십니까. 봉황객잔이 후기지수라면 홍화객잔은 이미 명성이 알려진 절정 고수. 특히 온천(溫泉)은 고관대작들도 한 번씩 다녀갈 정도의 명소지요.”

“온천?”

“저도 풍문으로만 들었는데, 극락이 따로 없답니다.”

총관이 잔잔한 목소리로 덧붙였다.

“저희 아버님께서 올해 팔순이신데, 한 번 오셨다가 극락으로 떠나실 뻔했습니다.”

“……그거 위험한 거 아니에요?”

“그만큼 좋다는 거지요. 아직 정정하십니다.”

“아, 예. 장수하셨으면 좋겠네요.”

온천이라…….

사우나는 자주 갔어도 온천은 한 번도 못 가 봤다. 뜨뜻한 물에 몸을 푹 담글 생각을 하니 벌써 설렌다.

“크흠. 그럼 가 볼까?”

“제가 모시겠습니다.”

총관을 따라 발걸음을 옮기려던 순간, 단단한 손아귀가 내 어깨를 덥석 붙잡았다.

“저어. 지금 온천이라고 하셨어요?”

“……아직 안 가셨어요?”

헤헤 웃는 청풍을 보며 확신했다.

이 자식이 온천은 처음이라는 것에 불알 두 쪽 건다.



* * *



이른 새벽, 아직 어둠이 짙게 깔린 저택의 연무장에는 한 사람이 검을 휘두르고 있었다.

이제 서른은 되었을까? 강건한 이목구비가 인상적인 사내였다.

쉬쉬쉭!

막힘없이 찌르고, 베고, 휘두른다. 초식과 초식이 바람에 꽃잎 휘날리는 듯 부드럽게 이어졌다.

어느덧 팔 성에 이른 칠매검(七梅劍)이 서늘한 새벽 공기를 가르고 있을 때, 전령(傳令) 하나가 대문을 열고 들어왔다.

“무슨 일이냐? 수련 중에는 출입을 금하였거늘.”

“송구합니다. 허나 상산왕(上山王) 전하께서 말씀을 전하라 하셔서…….”

“전하께서?”

“예. 금일 정오에 있을 오찬에 참석하라는 왕명이십니다.”

“오찬이라면…… 무림의 후기지수들이 온다는 그 자리냐?”

“옛.”

사내는 한숨을 푹 내쉬었다. 그는 정삼품 도지휘첨사(都指揮僉事)로, 관작으로 치면 능히 산서성에서 다섯 손가락 안에 꼽히는 인물이었다.

‘전하의 명이라 거절할 수도 없고. 이것 참.’

도지휘첨사는 결코 한가한 직위가 아니었다. 군사들의 훈련을 책임져야 하는 막중한 자리.

그러나 성주이자 고귀한 핏줄을 타고난 상산왕의 명령이다. 사내는 별수 없이 고개를 끄덕였다.

“왕명을 받들겠다고 전하여라.”

“충!”

전령이 떠나자 사내는 도로 검을 들었다.

다시 펼치기 시작한 칠매검에선 오래전 떠나온 화산(華山)의 매화가 피어오르는 듯했다.
```

## Final English reading copy

```markdown
# Chapter 136

“Ugh.”

“Gnnngh.”

The two men’s eyes met as they groaned. Seeing each other lying face down with their bare buttocks exposed was embarrassing, but it also gave them a strange sense of solidarity.

“Ahem. Young Hero Jeong, how are your wounds?”

“Ahem. More or less. How about you, Young Hero Gal?”

“I feel like I’m going to die, hngh!”

“Actually, same here, ngh!”

The pain returned as they spoke. Both men blinked back tears and muttered,

“There’s bad luck, and then there’s this. Out of all the people in the world, we had to run into the Sleeping Dragon of Shanxi.”

“I know. I never thought I’d suffer this kind of humiliation in my lifetime.”

The mood was gloomy.

In the Central Plains, where countless prestigious sects stood shoulder to shoulder, things might have been different. But out in borderland Shanxi Province, both men were heirs to sects big enough to swagger around spitting and farting as they pleased.

They had never once had to ask anyone for a favor or lower themselves in their entire lives. Now they were lying on a bed, groaning after being thoroughly beaten.

“Even when the Mount Heng Sword Sect was still standing, the Five Gates of Shanxi weren’t like this…”

“Those were the days.”

A few months ago, the Five Gates of Shanxi and the alliance of small and medium-sized sects could still have made their voices heard. Now, they couldn’t even squeak. The balance of Shanxi Murim had been shattered.

With the fall of the Mount Heng Sword Sect, the balance of power in Shanxi Murim was bound to tilt toward the Jin Family of Taiyuan.

“My father will kill me if he finds out.”

“Same here. He warned me so many times. If he finds out this happened… Ugh. I don’t even want to think about it.”

They had been publicly humiliated in front of more than a hundred people. By around New Year’s Day, the rumor would certainly have spread throughout all of Shanxi.

“If I had my way, I’d run far away.”

“To hell with running away. I don’t even know if I’ll be able to walk tomorrow. But I can’t refuse the City Lord’s summons, either…”

“Even if our legs are broken, we have to go. What else can we do? He isn’t just some ordinary City Lord. He’s a member of the imperial family.”

“That’s true. At least our faces are fine.”

“They are.”

Their eyes naturally shifted to the side.

Woo Jintae lay there as though dead, his face swollen like he had been stung by a swarm of wasps. If not for the occasional labored breath, they would have thought he was already dead.

“Still, how could anyone beat a person like that?”

“I never knew the Sleeping Dragon of Shanxi was this vicious.”

“Thank goodness we planted our heads on the floor beforehand. We almost ended up just like Brother Woo.”

“He absolutely would have done it. Isn’t he the bastard who beats women without mercy, too?”

There were two women among their group. A man might be expected to go soft in front of young, beautiful women, but that bastard Jin Taekyung’s reaction had gone far beyond anyone’s expectations.

“Age.”

“Y-yes?”

“Age. How old are you?”

“I-I’m seventeen.”

“And you?”

“I-I’m eighteen.”

Seventeen. Eighteen. They were both at the flower of their youth. They were also old enough for talk of marriage arrangements to begin circulating.

Just as everyone was wondering whether Jin Taekyung might be interested in the women, it happened.

“Lift your butt higher. You’ll break a bone.”

*Whack! Whack!*

“You kids are still wet behind the ears! And you’re already drinking!”

*Whack! Whack!*

“If you want to drink, hide somewhere and do it quietly! Don’t pick a fight with someone who was minding his own business!”

*Whack! Whack!*

“You haven’t learned how to behave! People like you are exactly why corporal punishment is necessary! Do you understand or not?”

*Whack! Whack!*

“Improve teacher authority! A certain amount of corporal punishment is absolutely necessary!”

*Whack! Whack! Whack!*

The two men trembled as they recalled what had just happened.

One had fainted, while the other had cried until tears and snot streamed down his face in front of everyone.

After having their buttocks thoroughly beaten by a man outside their families in front of so many people, it was only a matter of time before their marriage prospects were ruined.

“What in the world does ‘improve teacher authority’ mean? Is it something from Mencius?”

“I don’t know, either. He even hit me one extra time.”

“What a vicious bastard…”

“Even so, I envy the others.”

“What kind of outrageous thing is that to say? Can’t you see that your butt is covered in bruises?”

“At least the others were beaten by the Sleeping Dragon of Shanxi. I was beaten by some beggar-looking bastard… Sob!”

“Oh, that’s awful.”

“If I had been beaten by the Sleeping Dragon of Shanxi, I could have made excuses. But some mangy bastard whose origins I don’t even know beat my butt… What was he doing, borrowing a beating instead of money?”

His chin trembled with humiliation. He was thinking of the beggar-looking man who had taken the sword case from Jin Taekyung and gleefully thrashed him.

“Wow, this is fun! You have some good bounce in that butt!”

*Whack! Whack! Whack!*

“Does it hurt? How much does it hurt? If you don’t mind, can I hit you harder? This is my first time doing something like this, so please understand if I’m not very good at controlling my strength!”

*Whack! Whack! Whack!*

It was a moment of humiliation he would never forget—not until the day he died, and perhaps not even after death. If he could, he would have chewed that bastard from head to toe and swallowed him piece by piece, and it still wouldn’t have been enough.

“I will never forgive that bastard!”

“Don’t worry. I’ll help you however much I can, Young Hero Jeong!”

Who were they? They were the heirs of the Five Gates of Shanxi. Apart from Jin Taekyung of the Jin Family of Taiyuan, they had enough power to deal with a young beggar.

“Um, about that…”

“Yes?”

“Are you sure he really is a beggar? I’m not saying this because I’m afraid, but considering what happened with the Sleeping Dragon of Shanxi, I suddenly think there’s nothing to lose by preparing for the worst.”

“…Should we look into him a little more?”

“Y-yes. Let’s do that.”

The pampered rich kids had taken a group beating and finally learned to be cautious.

* * *

Once the lesson was over, we decided to move to a private room.

It was hard not to notice the eyes of the surrounding guests while we remained on the first floor.

Enjoying attention was fun for a moment or two, but if I tried to eat under these circumstances, I’d probably get confused about whether the food was going into my mouth or my nose.

“I’m Seok, the man responsible for Honghwa Inn. Please feel free to call me Chief Steward Seok.”

The Sleeping Dragon of Shanxi’s reputation really was something. The man in charge, who hadn’t shown even a trace of himself until now, had come to bow his head to me.

*This man must be part of the Lower District Sect, too, right?*

Honghwaru was Wolhwa’s base as the Chief Branch Leader of the Lower District Sect’s Shanxi branch, and Honghwa Inn was practically one of its subordinate organizations, as anyone could tell from the name.

He might even have known about my existence before I set foot inside Honghwa Inn.

*I can’t say that makes me feel particularly good.*

Was it overreacting to think that unseen gazes were monitoring my every move?

Still, I wasn’t exactly offended.

It was more like a little caution. We had certainly maintained a friendly relationship until now, but no one knew what might happen in the future.

“I’ve prepared a quiet place for you separately.”

“Oh, that sounds good.”

They were offering it as a courtesy, so there was no reason to refuse. I was just about to follow the chief steward when—

“Thank you for everything, Benefactor.”

I turned toward the voice and saw Cheongpung, wearing an innocent smile.

“What do you mean? Surely you aren’t planning to leave just like this?”

“Yes. It’s already late, so I was thinking of heading out.”

*Where does he think he’s going? We hadn’t even gotten to talk properly because those random bastards barged in.* I hurriedly waved him off. “Hey now, if it’s late, you should stay the night. You said you don’t have any travel money, right?”

“It’s all right. I’m used to sleeping rough.”

“You shouldn’t be used to that. Besides, this would be a new experience! Have you ever slept at an inn?”

“I stayed at an inn a few times before I lost my travel money. And I’ve already imposed enough on the two of you.”

Hyuk Mujin, who had been standing beside me, muttered,

“That’s true. With my candied hawthorn skewers[^1]—”

[^1]: Traditional fruit skewers coated in hardened sugar.

“You be quiet. So, are you really leaving?”

“Yes. Fortunately, I still have business left in Shanxi Province, so if we happen to get the chance, we’ll meet again.”

At this point, I had nothing left to say. If a Peak master was determined to leave of his own accord, I couldn’t exactly hold him back by claiming the roads were dangerous at night.

Even so, I was still intensely curious about the identity of this oddball who had suddenly appeared out of nowhere.

“If you have nowhere to go, come to the Jin Family of Taiyuan. If you give them my name, they’ll let you through.”

“Oh, now that you mention it, you’re a Young Master of the Jin Family of Taiyuan, aren’t you? The Sleeping Dragon of Shanxi, Jin Taekyung… I’ll remember the name of my Benefactor.”

He had known who I was for a while, yet he hadn’t reacted at all. His response amounted to, *Oh, I see,* and nothing more.

Hyuk Mujin subtly signaled me and cut in.

“The Jin Family of Taiyuan. You don’t know it?”

“Well, I think I’ve heard of it somewhere. It does sound familiar, but I don’t really know much about it.”

After tilting his head for a moment, Cheongpung bowed to us.

“If fate brings us together, we’ll meet again. Then I’ll be off.”

I replied with deep regret.

“Take care. And don’t forget the Jin Family of Taiyuan.”

“Haha, of course I won’t.”

He turned away with a hearty laugh. Thinking the conversation had come to an end, the chief steward spoke up.

“Then I’ll escort you to the annex.”

“Ah, yes. Mujin, let’s go.”

“Oh! We’re going to sleep in the annex of the famous Honghwa Inn?”

“We stayed in the annex at Phoenix Inn, too. Why are you acting like this is something new?”

“What are you talking about? If Phoenix Inn is a young prodigy, then Honghwa Inn is already a famous Peak master. Its hot springs, in particular, are such a renowned attraction that even high officials and nobles visit them.”

“Hot springs?”

“I’ve only heard about them from rumors, but they say there’s no paradise like it.”

The chief steward added in a calm voice,

“My father is turning eighty this year. He came here once and nearly departed for paradise.”

“…Isn’t that dangerous?”

“It only means the hot springs are that good. He’s still hale and hearty.”

“Ah, I see. I hope he lives a long life.”

Hot springs…

I had gone to saunas plenty of times, but I had never visited a hot spring. Just thinking about sinking into pleasantly hot water already had me excited.

“Ahem. Shall we go?”

“I’ll escort you.”

I was just about to follow the chief steward when a firm hand suddenly seized my shoulder.

“Um. Did you just say hot springs?”

“…You haven’t left yet?”

Looking at Cheongpung’s sheepish grin, I was certain of one thing.

I’d stake both my balls on the fact that this bastard had never been to a hot spring before.

* * *

In the early dawn, while darkness still blanketed the training ground of the estate, a man was swinging a sword.

He looked to be about thirty. His strong, rugged features were striking.

*Swish, swish, swish!*

He thrust, slashed, and swung without a moment’s hesitation. Each form flowed smoothly into the next, as softly as flower petals fluttering on the wind.

The Seven Plum Sword, in which he had reached eight-tenths mastery, cut through the cold dawn air when a messenger opened the main gate and entered.

“What is it? I forbade anyone from entering while I’m training.”

“I beg your pardon. His Highness Prince Shangshan ordered me to deliver a message…”

“His Highness?”

“Yes. It is the Prince’s command that you attend the luncheon at noon today.”

“The luncheon… You mean the gathering where the young prodigies of Murim are coming?”

“Yes, sir.”

The man let out a deep sigh. He was a Third-Rank Assistant Military Commissioner, an official who could easily be counted among the five highest-ranking figures in Shanxi Province.

*I can’t refuse an order from His Highness. What a nuisance.*

The position of Assistant Military Commissioner was by no means an idle one. It was a weighty office responsible for training the soldiers.

But the order had come from Prince Shangshan, the City Lord and a man of royal blood. The man had no choice but to nod.

“Tell him I accept the royal command.”

“Yes, sir!”

After the messenger left, the man picked up his sword again.

As he began the Seven Plum Sword once more, it seemed as though the plum blossoms of Huashan, which he had left behind long ago, were blooming from his blade.
```
