<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0118.txt",
      "sha256": "eab8effa058f2e84c45093cc4499ea1825b82cb934c035620b26a42880552744",
      "bytes": 12751
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "41014beeb02d7393d4d847311e8fbb4d755f6566e495dd76cff19d13a6ecc7d1",
      "bytes": 2510
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4e547e8e824ad836121184447cc3d274d236723d25157d0b56b1ba7cf7e10f29",
      "bytes": 18305
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "5deb3874a5bf873fc22fe5a6f884388270f3d379e6589cb15f2293b5835c5012",
      "bytes": 724
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "d019626cf2301584492b243a63ddcc51e5e2b6e0aaafb9dc9cb099ad0065c59b",
      "bytes": 1326
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "818f8065f826928398cc268616198b1faee3254b774e8929bcb4224abf3b338e",
      "bytes": 24117
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "4b4d7c8c1d1277b0680299a01a58cbee1ad96c32281e501b81a6453b586857f3",
      "bytes": 1040
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "05f382e9d41e20017da3ef8a0906bf0c8e1fdf371061791e6e550bbdbb8d6de0",
      "bytes": 17236
    }
  ],
  "estimated_tokens": 18517
}
-->

# Durable State Update — Chapter 118

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 118. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 118. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 118,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 118,
    "continuity_sources": [118],
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
    "Cheol Mubaek was critically injured after Pung Yang defeated him using a Temporary Strength Pill.",
    "Pung Yang possesses the Crimson Blood martial arts and has reached the Peak realm through them and the Temporary Strength Pill.",
    "Pung Yang can temporarily manifest imperfect Sword Force and can maintain powerful Body-Protecting Qi after taking the pill.",
    "Jin Mukyung is a young Peak-level swordsman known as the Heaven Shaking Sword.",
    "Jin Taekyung is a First Rate martial artist who uses One Annihilation with his iron spear.",
    "Jin Mukyung's visible duel with Pung Yang ended in Mukyung's favor, but Pung Yang's concealed throwing knives left Mukyung unconscious.",
    "Pung Yang killed more than ten Mount Heng Sword Sect martial artists after incapacitating Mukyung.",
    "Pung Yang plans to take both Jin brothers and obtain the Jin Family of Taiyuan's martial arts formulas.",
    "Jin Taekyung plans to use Jopil's Blazing Flame Divine Pill, which grants thirty years of internal energy but may kill its user through its fire qi.",
    "Lee Seowol and the surviving Mount Heng Sword Sect martial artists are approaching Pung Yang with weapons drawn."
  ],
  "continuity_sources": [
    117
  ],
  "open_questions": [
    "Can Jin Taekyung survive the Blazing Flame Divine Pill's fire qi and use its power?",
    "Can Taekyung defeat Pung Yang after the pill's effects are added to the fight?",
    "Will Jin Mukyung recover from the five concealed throwing knives?",
    "Can Lee Seowol and the Mount Heng Sword Sect survive Pung Yang's resumed assault?",
    "Will Pung Yang obtain the Jin Family's martial arts formulas?",
    "Will Lee Seowol's coerced marriage agreement be overturned?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What lasting consequences will the Blazing Flame Divine Pill have if Taekyung takes it?"
  ],
  "safe_through": 117,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Render 잠력단 as Temporary Strength Pill.",
    "Render 호신강기 as Body-Protecting Qi.",
    "Render 격산타우 as Striking the Ox Across the Mountain.",
    "Render 북망산 as Mount Beimang with a burial-ground footnote.",
    "Render 열화신단 as Blazing Flame Divine Pill.",
    "Render 반 갑자 as half a jiazi, clarified as thirty years.",
    "Retain Narye tagon for 나려타곤 with a footnote explaining the idiom."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 철무백    | **Cheol Mubaek**   |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 창법     | **spear technique**                              |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 기연     | **fortuitous encounter**                         | Use sparingly                                         |
| 살기     | **killing intent**                               |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 정파     | **orthodox faction**                             |                                                       |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 117
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 117
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang but was then incapacitated by five concealed throwing knives
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 117
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 117
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and can temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃118화



“너만 약 처먹으니까 좋았냐?”

“뭐?”

“혼자 약 처먹으니까 좋았냐고.”

풍양은 헛웃음을 흘렸다.

이제 고작 약관에 불과한 핏덩이 주제에 혀가 짧아도 너무 짧다. 태원진가의 막내 도련님으로 태어나 잠룡 소리를 듣고 있어 눈에 보이는 게 없는 건가?

“그놈 참, 허허.”

껍데기뿐인 웃음소리는 얼마 지나지 않아 잦아들고, 살기 어린 눈빛이 빈자리를 채웠다.

“관을 봐야 눈물 흘리겠느냐?”

진태경이 눈을 크게 떴다.

“이야, 저 대사 실제로 들으니까 되게 이상하네. 다시 해 봐.”

“말로 해선 안 되는 놈이군.”

풍양은 느긋한 걸음걸이로 다가가며 생각했다. 어떻게 해야 저 어린놈의 주둥이에서 살려 달라는 말이 나올까?

그가 평소 자주 사용하는 방법은 혀를 뽑고 사지를 잘근잘근 부러트리는 거다. 하지만 태원진가의 무공을 알려 줄 귀한 몸을 그리 함부로 대할 수가 있나.

적당한 타협이 필요했다.

‘다리 근맥을 끊어 놓으면 얌전해지겠지.’

태원진가와는 이미 돌이킬 수 없는 강을 건넜다. 풍양은 이 싸움이 끝나면 사람의 발이 닿지 않는 심산유곡에서 무공을 보완한 다음 다시 무림에 나올 생각이었다.

적풍단은 궤멸당했지만, 세력은 얼마든지 다시 모을 수 있다. 무림은 강자가 지배하는 곳이니까.

“전부 네가 자초한 일이니 날 원망 말거라.”

풍양이 곡도를 움켜쥔 그때였다.

“아, 잠깐만.”

손을 내저은 진태경이 뭔가를 입 안에 탁 털어 넣는다.

너무나도 자연스러운 모습에 풍양은 멈칫할 수밖에 없었다.

‘뭐 하는 거지?’

의문도 잠시.

한차례 몸을 부르르 떤 진태경의 전신에서 엄청난 열기가 피어오르기 시작했다.



* * *



어차피 내게 주어진 선택지는 하나밖에 없었다. 열화신단으로 최후의 도박을 벌이는 것.

위험성이 크긴 하지만 풍양에게 무공 구결을 토해 내고 죽는 것보다는 백배 나은 선택이다.

꿀꺽.

과연 영단은 영단인지, 혀에 닿자마자 스르륵 녹아 목으로 넘어간다. 문제는 그다음부터였다.

띠링.



- [열화신단]을 복용했습니다.

- [운기조식]으로 기운을 다스리십시오.



뜨겁다. 열화신단이 품고 있던 30년의 공력이 사지백해로 들불처럼 퍼져 나갔다.



- 일시적으로 [열양지기]의 속성을 부여받았습니다.

- 일시적으로 [공력]이 45년으로 상승합니다.

- 기운을 다스리지 못하면 죽음에 이를 수도 있습니다!

- 퀘스트, [영단 흡수]가 생성되었습니다.



끊임없이 울리는 시스템 알림을 확인할 여유 따위는 없었다. 당장 몸 안에서 날뛰는 열화신단의 기운을 제어하는 것만으로도 벅찼으니까.

“후우, 후우우우.”

인간 압력밥솥이 된 기분이다. 마치 정말 불이라도 난 것처럼 전신에서 연기가 모락모락 솟아올랐다.

딛고 선 땅 위로 덮여 있던 눈이 녹고, 축축한 흙이 물처럼 흐물흐물해졌다.

‘어느 정도 예상했지만 이건…….’

정말이지 상상 이상이다. 비명도 지르지 못하고 몸을 부르르 떠는 내 귓가로 풍양의 목소리가 파고들었다.

“무슨 짓을 한 거냐!”

당황한 놈의 얼굴을 보자 오히려 살짝 열기가 가라앉는 기분이다.

나는 억지로 입꼬리를 끌어 올리며 대답했다.

“무슨 짓이긴, 갈 데까지 가 보자는 거지.”

“놈!”

대답에서 불길함을 느낀 걸까? 풍양의 곡도가 눈부신 속도로 날아들었다. 쭉 뻗어 나온 붉은 도기(刀氣)가 내 가슴을 노린다.

쉭!

딱 반걸음 차이로 죽음이 빗겨 나간다. 목표를 놓친 곡도가 다시 한번 어지러운 궤적을 그렸다.

쉬쉬쉬쉭!

그러나 이번에도 곡도는 헛되이 허공을 갈랐다. 어느새 뒤로 물러난 나를 바라보는 풍양의 얼굴이 일그러졌다.

“너……!”

“뭐, 인마.”

애써 태연하게 대꾸했지만 사실 가장 놀란 건 나였다. 앞서 손을 섞었을 때는 이 정도로 손쉽게 피해 내지 못했다.

풍양의 압도적인 기세와 도기에 밀려 피하기에 급급했던 그때와는 차원이 다르다.

‘언제부터 몸이 이렇게 가벼웠지?’

공격을 피해야겠다고 생각한 순간, 몸이 그 어느 때보다 빠르게 움직였다. 달라진 것은 그뿐만이 아니다.

‘똑똑히 보인다.’

풍양의 움직임 하나하나가 보이고, 읽힌다. 공격이 보이니 못 피할 것도 없다. 도기가 아니라 도강(刀罡)이라 해도 피할 수 있을 것 같은 기분이다.

나는 마침내 그 이유를 깨달았다.

‘공력 때문이야.’

기존에 갖고 있던 15년의 공력과 열화신단의 30년 공력이 합쳐진 상태다. 비록 내가 완벽히 통제할 수는 없지만 그렇다고 해서 30년의 공력이 가진 힘이 없어지는 것이 아니다.

부풀어 오른 풍선처럼, 열화신단의 기운은 내 전신을 가득 채우고 있었다.

‘문제는 이 풍선이 언제 터질지 모른다는 거지만.’

그러니 그 전에 풍양을 쓰러트려야 한다.

나는 속에서 부글부글 끓어오르는 열기를 느끼며 철창을 고쳐 잡았다.

“덤벼.”

풍양이 입술을 깨물었다.

“어린놈이 벌써부터 기고만장하군. 네놈 정도로는 어림도 없다.”

“그런 것치곤 꽤 긴장한 것 같은데.”

“맹수는 토끼를 잡는 일에도 최선을 다하는 법이지.”

“근데 맹수는 토끼 잡을 때 잠력단 안 먹잖아.”

“……!”

풍양의 낯빛 위로 경악이 스쳤다. 입을 벌린 채 나를 응시하던 놈이 더듬더듬 물었다.

“자, 잠력단이라고?”

“그래, 잠력단.”

“그 이름을 네가 어떻게?”

“기업 비밀이다, 이 새끼야.”

“혹시 네놈도?”

“뭐, 비슷한 거 먹긴 했지.”

열화신단이라고 말하면 알까 모르겠다.

잠력단이랑 비교하면 안정성은 영 꽝이고, 효과가 어느 정도인지는 지금부터 알아볼 생각이다.

“넌 뒈졌어.”

마지막 한마디와 함께 땅을 박찼다.

쐐애애액!



* * *



풍양은 심란했다.

‘저놈이 어떻게 잠력단의 존재를 알고 있지?’

잠력단의 존재는 무덤까지 안고 가야 할 비밀이다.

언젠가 목숨을 구해 줄 숨겨 둔 한 수이기도 했지만, 세상에 알려진다면 피바람을 불러일으킬 기물(奇物)이기 때문이다.

복용자가 가진 힘의 두 배, 세 배를 끌어 올릴 수 있는 효능만 봐도 천하의 무인들이 군침을 삼키고 달려들 텐데.

그러나 그보다 더 큰 문제는 따로 있었다.

‘사마외도(邪魔外道)의 유산이니까.’

정마대전 이후 천하 무림은 정파 무림의 손아귀에 들어갔다.

풍양이 사마외도의 기연을 이었다는 소문이라도 퍼진다면 태원진가가 아니라 천하 무림이 그를 쫓기 시작할 것이다.

‘산서잠룡 진태경…… 반드시 죽여서 후환을 없애야 한다.’

풍양은 이를 악물고 무공을 펼쳤다.

단 몇 년간의 수련으로 어느덧 칠 성의 경지에 오른 적혈십이도(赤血十二刀)다. 나이로도, 무공으로도 턱없이 부족한 저 어린놈을 죽이기에는 차고 넘친다.

“죽엇!”

쉬잉-!

적혈십이도는 패도적인 무공, 곡도에서 쭉 뻗어 나간 붉은 도기가 사방을 난도질했다. 그 흉험한 기세에 땅거죽이 갈라지고, 바람이 터져 나갔다.

그러나 정작 베어야 할 목표는 이미 그곳에 없었다.

딱 반걸음 차이로 공격을 피해 낸 진태경이 창을 찔렀다.

쐐애애액!

목젖을 노리고 찔러 들어오는 창날. 황급히 고개를 꺾어 공격을 피한 풍양은 가슴 한구석이 서늘해졌다.

‘빠르다.’

빠르고 정확하다. 절정 고수의 상징인 검기상인(劍氣傷人)의 경지에까지는 이르지 못했지만 움직임은 이미 그를 따라잡고 있었다.

‘설마 이 녀석도 잠력단을? 아니다. 나와는 전혀 달라.’

이미 잠력단을 몇 번 복용한 전력이 있는 풍양이다.

전신이 시뻘겋게 달아오른 진태경의 모습으로 앞서 그가 삼킨 것이 잠력단이 아니라는 사실을 알 수 있었다.

‘그럼 도대체 뭘…… 헛!’

풍양은 생각을 이어 갈 수 없었다. 마침내 공세를 잡은 진태경이 본격적으로 진가창법을 펼쳐 내기 시작했기 때문이었다.

쉬쉬쉬쉬쉭!

소나기처럼 쏟아지는 수십 개의 창영(槍影). 보기만 해도 숨이 막히는 광경이다. 아니, 착각이 아니라 실제로도 그랬다.

풍양의 이마에서 땀 한 방울이 굴러떨어졌다.

‘이건…….’

열양지기.

그것도 절정 고수인 자신에게까지 영향을 줄 만큼 엄청난 열양지기다. 앞서 싸웠던 항산호 철무백도 열양지기의 소유자였지만 지금 진태경이 뿜어내는 것에 비할 바가 아니다.

‘영단, 열양 계열의 영단을 먹었구나!’

후우우웅!

알아챈다고 달라지는 것은 없었다. 아찔한 열기와 날카로운 공격. 연달아 물러서며 창날을 피하는 데에 급급하던 풍양이 입술을 질끈 깨물었다.

‘고작 이런 어린놈한테!’

일평생을 치열하게 살아온 그다. 잠력단까지 복용한 지금, 이제야 이름을 알리기 시작한 어린놈을 상대로 물러서는 자신이 수치스러웠다.

그 분노가 고스란히 곡도에 실렸다. 도신 위로 피어오른 도기가 그 어느 때보다 붉게 타올랐다.

쉬이익!

진가창법과 적혈십이도는 사용하는 병기와 투로는 다를지 몰라도 패도적인 무공이라는 공통점이 있다.

눈 깜빡할 시간, 진무경의 철창과 풍양의 곡도가 십여 합의 치열한 격돌 끝에 떨어졌다.

“음.”

먼저 물러난 것은 진태경이었다. 찢어진 손아귀에서는 피가 흘렀고, 무겁고 견고하던 철창은 예리한 도기에 잘려 나가 채 반도 남지 않았다.

“멍청한 놈.”

풍양은 득의양양한 웃음을 지었다. 무인이 병장기를 잃었다는 것은 패배를 의미했다.

오로지 권각으로 일가를 이룬 항산호 철무백도 자신에게 무릎을 꿇었는데, 아직 절정의 벽도 넘지 못한 진태경은 무기를 잃은 순간 이미 죽은 것이나 마찬가지다.

“정면 승부로 날 꺾을 수 있을 거라 생각했더냐?”

진태경이 손아귀에 묻은 피를 문질러 닦으며 대답했다.

“아니, 그 대신 귀중한 정보를 알았지.”

“……귀중한 정보?”

“그래, 너의 공격 패턴을 알았다.”

“패, 뭐?”

“너의 공격 패턴은 강강강강강이다.”

이건 무슨 개소린가.

자신의 무공에 관한 이야기라는 건 알겠는데 패 뭐시기라는 말은 난생처음 들어 본다. 게다가 강강강강강이라니?

풍양은 살기 어린 눈빛으로 진태경을 노려봤다.

“헛소리를 한 대가로 사지 근맥을 잘라 주마.”

진태경이 심드렁한 얼굴로 입을 열었다.

“사지 자르고 뽑는 거 되게 좋아하네. 사지 성애자야?”

“이 애새끼가…….”

“이 늙은 새끼가…….”

풍양은 깊게 심호흡했다. 그는 절정 고수였고 일평생을 냉철한 이성의 소유자로 살았다. 하지만 분노로 뚝뚝 끊기는 목소리만큼은 어쩔 수 없었다.

“넌, 반드시, 내 손으로, 죽인다.”

“난, 가끔, 사지를, 자른다, 가끔은, 이런 내가, 별로다.”

그는 인내심이 뚝 끊어지는 것을 느꼈다. 단언컨대 근 십 년간 이 정도로 분노한 적은 처음이다.

“크아아악!”

비명인지 고함인지 모를 괴성을 내지른 풍양은 광인(狂人)처럼 돌진했다.

그 어떤 초식도, 무공도 없이 있는 힘껏 진태경의 정수리 위로 곡도를 내리쳤다.

“죽엇!”

그때였다. 살기로 번들거리는 풍양의 핏빛 눈동자에 진태경의 담담한 표정이 비친 것은.

순간 찬물을 뒤집어쓴 것처럼 정신이 번쩍 들었다.

‘뭔가 잘못됐다.’

풍양은 공력을 있는 힘껏 끌어올렸다.

호신강기가 일어남과 동시에 텅 비어 있던 진태경의 손아귀에서 비수가 번쩍였다.

푹!
```

## Final English reading copy

```markdown
# Chapter 118

“Was it fun being the only one shoving pills down your throat?”

“What?”

“I asked if it was fun shoving pills down your throat all by yourself.”

Pung Yang let out a hollow laugh.

*For a mere brat barely twenty, his speech was far too disrespectful. Had being born the youngest young master of the Jin Family of Taiyuan and being called the Sleeping Dragon made him think he could get away with anything?*

“What a brat. Heh.”

The empty laughter soon died away, and murderous eyes took its place.

“Must you see the coffin before you shed tears?”

Jin Taekyung’s eyes widened.

“Wow, hearing that line in real life makes it sound really weird. Try it again.”

“You’re a brat who can’t be reasoned with.”

As he approached at a leisurely pace, Pung Yang wondered how he could make that young brat beg for his life.

His usual method was to pull out the tongue and slowly break all four limbs. But he couldn’t treat a valuable body that knew the Jin Family of Taiyuan’s martial arts so carelessly.

A reasonable compromise was necessary.

*If I sever the meridians in his legs, he’ll quiet down.*

He had already crossed an irreversible river with the Jin Family of Taiyuan. Once this fight was over, Pung Yang planned to retreat into some remote mountain valley untouched by human feet, refine his martial arts, and then return to the Murim.

The Red Wind Band had been annihilated, but he could gather a force again whenever he wanted. The Murim was a place ruled by the strong, after all.

“Everything that happened was brought on by you, so don’t blame me.”

Pung Yang was just tightening his grip on the curved saber when—

“Ah, wait a second.”

Jin Taekyung held up a hand, then casually tossed something into his mouth.

The action was so natural that Pung Yang couldn’t help stopping.

*What is he doing?*

His question was answered a moment later.

After Jin Taekyung’s body shuddered once, tremendous heat began to rise from every inch of him.

* * *

I had only one option left.

To make one last gamble with the Blazing Flame Divine Pill.

It was a dangerous choice, but it was a hundred times better than dying after being forced to spit out the Jin Family’s martial arts formulas for Pung Yang.

Gulp.

True to its name, the divine elixir melted the moment it touched my tongue and slid down my throat. The problem began after that.

*Ding.*

> **System**
> - You have taken the **Blazing Flame Divine Pill**.
> - **Circulate your qi** to control your energy.

It was hot. The thirty years of internal energy contained within the Blazing Flame Divine Pill spread through every part of my body like wildfire.

> **System**
> - You have temporarily gained the **Scorching Yang Qi** attribute.
> - Your **internal energy** has temporarily increased to 45 years.
> - If you cannot control your energy, you may die!
> - Quest, **Divine Pill Absorption**, has been created.

I had no time to check the System notifications that continued ringing in my ears. Controlling the Blazing Flame Divine Pill’s energy rampaging through my body was already more than enough.

“Hoo. Hooooo.”

I felt like a human pressure cooker. It was as though a real fire had broken out inside me, and wisps of smoke rose from my entire body.

The snow covering the ground beneath my feet melted, and the damp earth softened until it flowed like water.

*I expected something this bad, but this is…*

It was far beyond my imagination. I couldn’t even scream. I could only tremble as Pung Yang’s voice pierced my ears.

“What have you done?”

Seeing the bewilderment on his face actually made the heat subside a little.

I forced the corners of my mouth upward and answered.

“What else? I’m going all in.”

“You brat!”

Had he sensed something ominous in my answer? Pung Yang’s curved saber flew toward me at a blinding speed. A red strand of saber qi extended from the blade and aimed for my chest.

*Swish!*

Death passed me by at a distance of exactly half a step. The curved saber missed its target and drew another chaotic arc.

*Shh-shh-shh-shhk!*

But once again, the blade only cut through empty air. Pung Yang’s face twisted as he stared at me, already backed away.

“You…!”

“What, asshole?”

I answered as casually as I could, but the person most surprised was me. When we had crossed hands earlier, I hadn’t been able to dodge so easily.

This was on an entirely different level from before, when Pung Yang’s overwhelming aura and saber qi had forced me to do nothing but evade.

*Since when has my body felt this light?*

The instant I thought I needed to avoid an attack, my body moved faster than ever before. And that wasn’t the only thing that had changed.

*I can see everything clearly.*

I could see and read each of Pung Yang’s movements. If I could see the attacks, there was no reason I couldn’t evade them. I felt like I could dodge even saber force, not just saber qi.

At last, I understood why.

*It’s because of my internal energy.*

My original fifteen years of internal energy had merged with the thirty years from the Blazing Flame Divine Pill. I couldn’t control it perfectly, but that didn’t mean the power of thirty years of internal energy had simply disappeared.

Like an overinflated balloon, the Blazing Flame Divine Pill’s energy filled my entire body.

*The problem is that I have no idea when this balloon will burst.*

So I had to take down Pung Yang before that happened.

Feeling the heat bubbling up inside me, I adjusted my grip on the iron spear.

“Come at me.”

Pung Yang bit his lip.

“Young brat, you’re already getting cocky. Someone like you is nowhere near strong enough.”

“You look pretty tense for someone saying that.”

“A wild beast gives its all even when catching a rabbit.”

“But a wild beast doesn’t take a Temporary Strength Pill to catch a rabbit.”

“...!”

Shock flashed across Pung Yang’s face. He stared at me with his mouth hanging open, then stammered.

“Y-You mean the Temporary Strength Pill?”

“Yeah. The Temporary Strength Pill.”

“How do you know that name?”

“Corporate secret, asshole.”

“Did you take one too?”

“Well, I did eat something similar.”

I wondered whether he would recognize the name if I called it the Blazing Flame Divine Pill.

Compared to the Temporary Strength Pill, its stability was complete garbage. I intended to find out exactly how powerful its effects were starting now.

“You’re fucking dead.”

With those final words, I kicked off the ground.

*Shweeeeeek!*

* * *

Pung Yang was deeply troubled.

*How does that brat know about the Temporary Strength Pill?*

The existence of the Temporary Strength Pill was a secret he had to take to his grave.

It was a hidden trump card that might save his life someday. But if its existence became known, it would be a wondrous object capable of bringing a bloodbath to the entire world.

Just the fact that it could draw out two or three times the power of the person who took it would be enough to make martial artists throughout the land salivate and come running.

But there was an even greater problem.

*It’s a legacy of demonic, heterodox arts.*

After the Great Faction War, the Murim had fallen into the hands of the orthodox factions.

If even a rumor spread that Pung Yang had inherited the legacy of demonic, heterodox arts, it wouldn’t be only the Jin Family of Taiyuan pursuing him. The entire Murim would come after him.

*Jin Taekyung, the Sleeping Dragon of Shanxi… I must kill him and eliminate the trouble he’ll cause later.*

Pung Yang gritted his teeth and unleashed his martial arts.

After only a few years of training, he had already mastered seventy percent of the Crimson Blood Twelve Sabers. That was more than enough to kill a brat hopelessly beneath him in both age and martial arts.

“Die!”

*Shiiing!*

The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart.

Yet the target he needed to cut was no longer there.

Jin Taekyung dodged the attack by exactly half a step and thrust his spear.

*Shweeeeeek!*

The spearhead drove toward Pung Yang’s throat. Pung Yang hastily twisted his head aside to evade it, and a chill settled in his chest.

*Fast.*

Fast and accurate. He had yet to reach the stage where Sword Energy could injure a person—the hallmark of a Peak master—but his movements had already caught up to Pung Yang’s.

*Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.*

Pung Yang had already taken the Temporary Strength Pill several times.

From Jin Taekyung’s body, which had turned bright red with heat, Pung Yang could tell that what he had swallowed earlier was not the Temporary Strength Pill.

*Then what did he… Wait!*

Pung Yang couldn’t continue thinking. Jin Taekyung had finally seized the initiative and begun to unleash the Jin Family’s Spear Technique in earnest.

*Shh-shh-shh-shh-shhk!*

Dozens of spear shadows poured down like a rain shower. It was a suffocating sight.

No, it wasn’t just an illusion. It really was suffocating.

A bead of sweat rolled down Pung Yang’s forehead.

*This is…*

Scorching Yang Qi.

And not just any Scorching Yang Qi—it was powerful enough to affect even Pung Yang, a Peak master himself. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now.

*He ate a divine elixir—a Scorching Yang-type divine elixir!*

*Whooooom!*

Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he repeatedly retreated, barely managing to evade the spearhead.

*Against a brat this young!*

He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself.

That anger flowed straight into his curved saber. The saber qi rising over the blade burned redder than ever.

*Hiss!*

The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in their weapons and forms, but they shared one thing in common: both were domineering martial arts.

In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges.

“Hmm.”

Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained.

“You fool.”

Pung Yang smiled triumphantly. A martial artist losing their weapon meant defeat.

Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation entirely with his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm yet. The moment he lost his weapon, he was as good as dead.

“Did you think you could defeat me in a head-on fight?”

Jin Taekyung rubbed the blood from his palm and answered.

“No. But I did learn some valuable information.”

“...Valuable information?”

“Yeah. I learned your attack pattern.”

“Pat—what?”

“Your attack pattern is strong, strong, strong, strong, strong.”

*What kind of bullshit is this?*

Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong?

Pung Yang glared at Jin Taekyung with murderous eyes.

“I’ll sever the meridians in all four of your limbs as payment for talking nonsense.”

Jin Taekyung opened his mouth with a bored expression.

“You really like cutting off and pulling out people’s limbs. Are you a limb fetishist?”

“You little brat…”

“You old bastard…”

Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger.

“You. Will. Die. By. My. Hand.”

“I. Sometimes. Cut off limbs. Sometimes, I don’t like this version of myself.”

He felt his patience snap. He could swear that he had never been this furious in nearly ten years.

“Graaaargh!”

Pung Yang charged like a madman, emitting a howl that could have been either a scream or a roar.

Without using a single form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength.

“Die!”

That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent.

In an instant, his mind snapped clear as though someone had dumped cold water over him.

*Something’s wrong.*

Pung Yang drew up his internal energy with all his might.

As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand.

*Shnk!*
```
