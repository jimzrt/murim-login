<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0152.txt",
      "sha256": "fa9e18fb9c3ca54c07b8cc85b0f1f26417de9eb5f521c0d4c10e5889c8a5cd72",
      "bytes": 13065
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "47f72db2cbe8b75e5fa2475dc5f79204f90cee037d864a22ccf767a026da92c8",
      "bytes": 5994
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4614241e3160aec1adb57d303421962b0b4a36ed6a2681bc20d26d154610773d",
      "bytes": 34438
    },
    {
      "path": "characters/Childeuk.md",
      "sha256": "5702ed20c07f8be566262b26d8445b983e160e5f0abe95e9093b8c25037f30d2",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b193fb5db398d3a98898e3370f603fe2c0f30fa9b83d12220350670699923dbc",
      "bytes": 28865
    }
  ],
  "estimated_tokens": 25509
}
-->

# Durable State Update — Chapter 152

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 152. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 152. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 152,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 152,
    "continuity_sources": [152],
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
    "The City Lord's luncheon attendance requirement has concluded; Prince Shangshan's Token was obtained as the Quest Reward, and Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, has no martial title yet, and has begun teaching Taekyung and Hyuk Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is a first-generation Huashan disciple known as Huashan's Lone Crane and the first of the Three Plum Blossom Elites; he met Cheongpung ten years ago and is traveling with the other Elites to meet him again.",
    "Chulwoo and Eunhyang are Baek Museong's junior disciples and fellow members of the Three Plum Blossom Elites; both are notorious troublemakers who caused trouble with the Black Serpent Sect while traveling.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung's side; they will remain at Honghwa Inn until New Year's Day.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao's autograph request three years earlier; Taekyung now promises to obtain Mukyung's autograph for Zhu Bao at the upcoming banquet.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away, faces a large administrative workload, and prefers practical people with flexible thinking over rigid scholars; Hong Jin gave him one thousand silver nyang, prompting an extravagant pro-imperial welcome and a joking rapport between them.",
    "Jin Mukyung lost to Cheongpung four days before this chapter, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Jin Taekyung now has a private training ground in a newly rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung."
  ],
  "continuity_sources": [
    151,
    150
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?"
  ],
  "safe_through": 151,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation; render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” and 환골탈태 as “Bone Transformation.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” and 찍고 땡 as “touch-and-go method.”"
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
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 찍고 땡 | **touch-and-go method** | Repeatedly reaching a destination and returning as an endurance exercise. |

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
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 철우 | 백무성 | junior_disciple_to_senior_brother | Senior Brother | deferential | Uses 대사형 while answering Baek Museong. |
| 은향 | 백무성 | junior_disciple_to_senior_brother | Big Brother; Senior Brother | familiar and casual-polite | Repeatedly calls him 큰 오라버니 even after he insists on 대사형. |

## Exact glossary matches

| 태원진가   | **Jin Family of Taiyuan**        |
| 하북팽가   | **Hebei Peng Family**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 대주     | **Squad Leader** / **Commander**             |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |

## Listed compact profiles

### Childeuk.md

# Childeuk (칠득이)

- **Safe through:** Chapter 135
- **Aliases:** None
- **Role:** Illiterate Level 15 martial artist and servant of the Jin Family of Taiyuan, directly under Jin Wikyung; publicly advocates for the family's reputation
- **Personality:** Physically strong, diligent, gullible, and intensely excitable; readily interprets praise as recognition of exceptional talent
- **Voice:** Deferential, overeager, and breathless when speaking to Jin Wikyung
- **Relationships:** Servant under Jin Wikyung; assigned to serve Jin Mukyung and Jin Taekyung until removed from meal delivery after a misunderstanding

## Korean source

```text
＃152화



“흐아아아암.”

늘어져라 하품을 한 중년 무인이 옆을 흘끗 바라봤다.

몇 걸음 떨어지지 않은 곳에 오늘 새로 발령받은 신참이 뻣뻣한 자세로 정면을 주시하는 중이었다.

‘그놈 참. 떡대 하나는 끝내주네.’

절굿공이 같은 팔다리 하며, 딱 벌어진 어깨 하며.

덩치만 보면 근골 좋기로 유명한 하북팽가(河北彭家) 출신은 아닌지 의심이 들 정도였다.

‘그러고 보니 아직 이름도 모르는군.’

날은 춥고, 근무 시간은 앞으로 세 시진도 더 남았다.

이런 날에는 주둥이라도 털어야 시간도 금방 가고 몸도 따뜻해지는 법. 중년 무인이 슬그머니 입을 열었다.

“여보게.”

“예, 옛!”

“어허, 벽력탄을 삶아 먹었나. 왜 이리 목청이 커?”

“죄송합니다!”

“그렇다고 사과할 것까진 없고. 신입이라 그런가? 패기 넘치는 모습이 보기 좋구먼.”

“헛, 감사합니다.”

“응. 그려, 그려.”

중년 무인은 흐뭇하게 웃었다. 몇 마디 안 나눠 봤지만 괜찮은 놈 같다. 행동거지가 우직하고, 요즘 젊은것들답지 않게 예의도 바르다.

슬슬 뒷방 늙은이 취급받는 처지인 그로서는 꽤 괜찮은 말동무가 생긴 셈이었다.

“혹시 자네 성이 팽가인가?”

“아닙니다. 장가입니다.”

“혹시나 해서 물어봤네. 자네 근골이 좀 좋아야지. 난 또 하북팽가의 먼 방계라도 되나 싶었지 뭔가.”

신참 무인이 뒤통수를 긁적였다.

“제가 코흘리개 때부터 힘깨나 쓰긴 했지요.”

“어쩐지. 팔다리에 아주 근육이 옹골차네그려. 내 젊을 때를 보는 것 같아.”

물론 턱도 없는 소리다. 하지만 생긴 것답지 않게 제법 눈치가 있는 신참 무인은 넙죽 허리를 숙였다.

“선배님께서 젊으셨을 적에 비하면 저는 아무것도 아닙니다.”

“어허. 선배가 뭔가, 앞으로는 형님이라고 부르게. 아, 나는 홍가일세.”

“예, 형님!”

“허허. 좋은 아우가 생겼구먼. 그래, 우리 장 아우는 본가에 언제 입문(入門)했는가?”

“벌써 수년 되었습니다.”

“으잉? 그럴 리가, 아우 같은 장군감이 들어왔으면 내가 진작 알았을 터인데…….”

어언 이십 년을 태원진가에 몸담은 그다. 나름 터줏대감이라 무인 중 누가 들어오는지, 누가 나가는지는 정확히 알았다.

“아, 무인이 된 건 한 달도 안 됐습니다. 그전에는 하인으로 잡일이나 이것저것 했었죠. 눈에 잘 안 띄는 곳이라 모르셨을 수도 있습니다.”

“아아, 그랬구먼.”

중년 무인은 새삼스러운 눈빛으로 신참을 바라봤다.

하인에서 무인이라. 아주 없는 일은 아니지만 그렇다고 흔한 일도 아니다.

“뒷배가 좋나 보군.”

“예?”

“예끼, 알 만한 사람이 시치미 떼기는. 신참이 이 자리에 들어오는 게 쉬운 일인 줄 알아?”

중년 무인이 씩 웃으며 신참의 옆구리를 쿡쿡 찔렀다.

“누군가? 내총관이야 워낙 깐깐한 위인이니 아닐 테고, 수뇌부에 튼튼한 줄이라도 하나 잡았나?”

“저, 그게…….”

“나만 알고 있을 테니 살짝 말해 보게. 외당주인가? 아니면 철검대주?”

아뇨, 소가주님께서 보내셨는데요.

신참 무인, 장칠득은 튀어나오려던 말을 꿀꺽 삼켰다.

사람의 입이 얼마나 가벼운가, 곧이곧대로 말했다가는 내일 해가 뜨기 전에 소문이 퍼질 것이 뻔했다.

‘소가주님께 누를 끼칠 수는 없다!’

태원진가에 대한 충성심 하나만큼은 여느 열사(烈士) 못지않은 칠득이다.

그는 궁금함이 잔뜩 담겨 있는 중년 무인의 눈빛을 외면하며 입을 열었다.

“그런데 여기가 그렇게 들어오기 힘든 곳이었습니까?”

칠득의 화제 전환에 중년 무인이 실망한 표정으로 입맛을 다셨다. 굳이 말하기 싫다는데 더 찔러 보기도 뭐하다.

“쩝. 자네, 본가에 몇 년 동안 있었다고 했지?”

“그렇죠. 하인이었지만.”

“그럼 그 몇 년간 수련동에 몇 번이나 와 봤나?”

“딱 두 번 와 봤습니다.”

“그렇지? 자, 그 자리에서 한 바퀴 쓱 둘러보게.”

“지금요?”

“그럼 내년에 할래?”

장칠득은 시키는 대로 주위를 둘러봤다. 태원진가의 뒤를 빈틈없이 감싼 가파른 절벽 아래, 뻥 뚫려 있는 동공(洞空).

그곳이 수련동의 입구였고, 그와 중년 무인 외에는 아무도 없었다.

“어떤가?”

“휑하네요.”

“그렇지? 여기 하루에 몇 명이나 올 것 같나?”

“몇 명이나 옵니까?”

중년 무인이 심드렁하게 대답했다.

“안 와.”

“예?”

“네 시진마다 교대하러 오는 인원 제외하면 아무도 안 온다고. 아, 식사 전해 주는 하인도 있었군.”

“하지만…… 수련동이잖습니까?”

“수련동이지. 그런데 여기서 수련하는 사람? 없어. 예전에 삼공자가 사고 치고 몇 번 들락거리긴 했지만.”

이 무슨 황당무계한 말인가. 그러고 보니 말만 수련동이지, 막상 이곳에서 수련했다는 사람은 못 본 것 같다.

반면 연무장은 사시사철 무인들로 득실거렸다.

“그럼 여길 왜 지키는 겁니까?”

“상징이지.”

“상징이요?”

“먼 옛날, 본가를 세우신 진무량 조사(祖師)께서 수련하시던 곳이거든. 전해지기로는 이 절벽에서 수련하시던 도중 문득 깨달음을 얻어 무공을 펼쳤는데, 일격에 절벽 밑이 뻥 뚫렸다는군.”

장칠득은 입을 딱 벌렸다.

진무량 조사에 대한 전설은 그도 들어 본 기억이 있다. 삼백 년 전에는 천하에서 손꼽히는 고수였다던가?

하지만 어찌 인간의 몸으로 그것이 가능하단 말인가.

“그, 그게 사실입니까?”

“자그마치 수백 년 전의 일일세. 사실이면 어떻고, 거짓이면 어떤가? 정작 중요한 사실은 따로 있는 것을.”

“……예?”

“이 수련동 앞에서 하루 몇 시진만 죽치고 앉아 있으면 월봉이 따박따박 나온다는 것. 그게 중요한 걸세. 시간이 더럽게 안 가는 게 흠이긴 하지만.”

씩 웃은 중년 무인이 장칠득의 어깨를 두드렸다.

“축하하네. 자네는 본가의 무인들이 꿈꾸는 최고의 보직에 임명된 걸세. 일명 꿀보직이라고 하지.”

“…….”

장칠득의 얼굴이 일그러졌다. 곧 은퇴해도 이상하지 않을 나이라면 모를까, 지금처럼 한창때에 할 일 없이 수련동에서 시간이나 죽이고 있을 생각은 없다.

그의 생각을 알 리 없는 중년 무인은 품에서 육포 하나를 꺼내어 씹었다.

“자네도 하나 줘?”

“전 괜찮습니다.”

“왜? 짭조름하니 괜찮은데. 육포 씹으면서 하늘 보면 시간도 금방 가고 좋아.”

수련동 입구에 비스듬히 기댄 중년 무인이 고개를 꺾어 하늘을 바라봤다.

“아따, 하늘 한번 맑다. 보고만 있어도 가슴이 탁 트이네.”

장칠득도 마지못해 위를 흘끗 바라봤다.

중년 무인의 말처럼 날씨는 맑았다. 푸른 하늘 위, 천천히 흘러가는 조각구름과 검은 점 몇 개가 떠다녔다.

“저건 뭡니까?”

“새겠지, 뭐.”

멍하니 하늘을 바라보던 장칠득의 시선이 까마득한 높이의 절벽을 향했다. 문득 그의 눈이 가늘어졌다.

“절벽에 붙어 있는 저건요?”

“절벽? 절벽에 뭐가 있나?”

“예. 꽤 큰데요?”

“몰러. 꽤 큰 새인가 보지. 가만있자, 술을 한 병 가져왔는데…….”

중년 무인은 칠득이 가리키는 곳을 쳐다보지도 않고 품에서 조그마한 자기 병 하나를 꺼내 들었다.

“새치고는 좀 너무 큰 것 같은데요.”

“천응(天鷹)이라는 놈일 수도 있지. 그놈들은 덩치가 사람만 하거든. 보통 매가 아니여.”

“허어, 진짜 사람만 하네요.”

“영물 소리도 듣는 놈이니까. 날개 길이만 일장이 넘는다고 하던데, 나도 멀리서 딱 한 번 봤네.”

“그런데 형님.”

“아, 왜 자꾸 부르나?”

“천응도 떨어집니까?”

“그게 뭔 개소리여?”

술병을 기울이던 중년 무인이 황급히 절벽을 쳐다봤다. 까마득한 높이, 거대한 점이 빠르게 추락하고 있었다.

“으아아아아악!”

장칠득이 감탄했다.

“영물은 영물이네요. 비명이 꼭 사람 같습니다.”

“저거 사람이야, 이 미친놈아!”

“뜨아아!”

“피해, 피해!”

중년 무인이 비명을 내지른 다음 순간, 비처럼 쏟아지는 돌조각과 함께 한 사람이 지면에 추락했다.

쾅! 후두두둑!

돌과 먼지가 사방으로 비산했다. 두 사람이 동시에 침을 꼴깍 삼켰다.

“주, 죽은 걸까요?”

“저 높이에서 떨어져 봐. 옥황상제도 죽는다.”

평온하던 일상에 이 무슨 참담한 사태란 말인가.

중년 무인은 떨리는 가슴을 부여잡고 엎어진 시신을 바라봤다.

“도대체 어떤 미친놈이 절벽에서…….”

“젊은 놈 같은데요?”

“지금 젊은 놈이건 늙은 놈이건 그게 중요한가? 죽었다는 게 중요하지.”

“그건 그렇지만…….”

“가서 한 번 뒤집어 보게.”

“제, 제가 말입니까?”

“여기 자네랑 나 말고 누가 있나? 어서!”

중년 무인의 호통에 장칠득이 머뭇거리며 시신을 향해 다가가기 시작했다.

무인이 된 지 고작 한 달. 눈앞에서 사람의 죽음을 목도한 것은 이번이 처음이다.

“후욱, 후욱.”

가까워질수록 시신의 모습이 명확하게 보이기 시작한다.

축 늘어진 사지, 엎어진 뒤통수에서는 핏물이 줄줄 흘러내렸다. 저 높이에서 떨어진 것치고는 곱게 죽은 모습.

“그, 극락왕생하시오.”

눈을 질끈 감고 시신의 몸에 손을 댄 그 순간이었다.

벌떡, 빡!

눈앞이 번쩍하더니 격통이 밀려들었다.

그대로 엉덩방아를 찧은 장칠득은 자신이 쌍코피를 흘리는 것도 모르고 입을 딱 벌렸다.

“어어, 어어어.”

“갑자기 뭔…… 으어어, 으어어어!”

중년 무인도 다리에 힘이 풀려 털썩 쓰러졌다.

“시체가, 시체가 살아 있다!

“으어어, 강시다! 강시가 나타났다!”

시체, 강시.

졸지에 죽은 놈이 되어 버린 흙투성이의 괴인이 비틀거리며 일어났다.

산발이 된 머리, 실핏줄이 터진 눈동자로 주위를 둘러보던 그가 빠드득, 이를 갈았다.

“씨벌, 또 태초 마을이야?”



* * *



더럽게 아프네.

머리, 어깨, 무릎, 발, 무릎, 발…… 안 쑤시는 곳이 없다. 그나마 절벽에 단검을 박아서 추락 속도를 늦춰 망정이지, 하마터면 골로 갈 뻔했다.

물론 꾸준하게 올려놓은 근골, 맷집 스탯도 한몫했고.

“어우, 뒷골 땡겨.”

따끔한 뒤통수를 만져 보니 핏물이 축축하게 묻어 나온다.

소매를 북 찢어 피를 닦아 내던 그때였다.

“누, 누구냐!”

“정체, 정체를 밝혀라, 이노옴!”

아, 이 아저씨들도 있었지.

대뜸 칼을 들이대는 두 사람 중 한 명의 얼굴이 낯이 익다. 그러니까 이름이…….

“장칠득?”

며칠 전까지만 해도 홍화객잔에서 여론 조작에 힘쓰시던 장칠득 씨가 기겁하며 물러났다.

“허억! 어떻게 내 이름을?!”

“강시가 말을 한다! 말로 사람을 홀린다!”

“……누가 강시야. 숨 잘만 쉬고 있는 거 안 보여요?”

수염이 듬성듬성한 중년 아재가 눈을 부릅뜨며 외쳤다.

“이 사악한 것! 내 눈을 속일 수는 없다. 네가 사람이라면 저 높이에서 떨어지고도 멀쩡할 리 없을 터, 어디서 보냈느냐! 마교(魔敎)? 혈교(血敎)? 그것도 아니면…….”

“태초 마을! 형님, 저 강시가 분명 태초 마을이라고 했습니다.”

“그렇지! 태초 마을에서 보낸 강시구나!”

감 잡았다는 듯이 버럭 소리친 중년인이 순간 멈칫하더니 장칠득에게 물었다.

“그런데 태초 마을이 어디야?”

“저도 모르죠.”

“…….”

알면 이상하지.

나는 대화를 포기하고 흙투성이가 된 얼굴을 옷소매로 문질렀다.

중년인은 몰라도 장칠득은 내 얼굴을 잘 아니까 이게 더 빠르겠지.

“헉, 삼공자님!”

“네, 오랜만이에요.”

“아우, 삼공자님이라니. 그게 대체 무슨 소린가?”

“삼공자님이 강시가 됐습니다!”

“…….”

결론이 왜 그따위냐.
```

## Final English reading copy

```markdown
# Chapter 152

“Yaaawn.”

A middle-aged martial artist glanced to the side after letting out a long yawn.

Only a few paces away, the new recruit who had been assigned here today was standing stiffly and staring straight ahead.

*What a guy. He’s got one hell of a build.*

Limbs like pestles. Shoulders spread wide.

Judging by his size alone, one might have suspected he came from the Hebei Peng Family, famous for producing martial artists with strong bones and muscles.

*Come to think of it, I don’t even know his name yet.*

The weather was cold, and there were still more than three shichen left in his shift.

On days like this, chatting was the best way to make time pass faster and keep warm. The middle-aged martial artist slowly opened his mouth.

“Hey there.”

“Yes, sir!”

“Good heavens, did you swallow a thunderbolt? Why are you shouting so loudly?”

“I’m sorry!”

“You don’t have to apologize for that. Is it because you’re new? It’s nice to see someone so full of spirit.”

“Ah, thank you.”

“Yeah, yeah. That’s right.”

The middle-aged martial artist smiled, pleased. They had only exchanged a few words, but the kid seemed decent. His manner was straightforward, and unlike young people these days, he was polite too.

For a man who was slowly being treated like an old-timer fit only for the back rooms, he had found himself a pretty good conversational partner.

“Is your surname perhaps Peng?”

“No. It’s Jang.”

“I only asked because I was curious. Your physique is quite impressive. I wondered whether you might be from some distant collateral branch of the Hebei Peng Family.”

The new martial artist scratched the back of his head.

“I was pretty strong even when I was a little kid.”

“I thought so. Your limbs are packed with muscle. You remind me of myself when I was young.”

Of course, that was utter nonsense. But despite his appearance, the new martial artist was perceptive enough to immediately bow deeply.

“Compared to what you were like in your youth, Senior, I’m nothing.”

“Hey, none of this ‘Senior’ business. Call me hyung from now on. Ah, I’m Hong.”

“Yes, hyung!”

“Heh heh. Looks like I’ve got myself a good little brother. So, Jang, when did you join this family?”

“It’s already been several years.”

“Huh? That can’t be right. If a fine candidate for a general like you had joined, I would have heard about it long ago…”

He had been with the Jin Family of Taiyuan for nearly twenty years. He considered himself something of an old hand and knew exactly which martial artists came and went.

“Ah, I haven’t even been a martial artist for a month. Before that, I was a servant who handled odd jobs here and there. I worked in places where I didn’t stand out much, so you might not have noticed me.”

“Ahh, I see.”

The middle-aged martial artist looked at the new recruit with fresh interest.

A servant who became a martial artist. It wasn’t unheard of, but it wasn’t common either.

“You must have a powerful backer.”

“Pardon?”

“Oh, come on. Don’t play dumb. Do you think it’s easy for a new recruit to get assigned to this position?”

The middle-aged martial artist grinned and poked the new recruit in the side.

“Who is it? The Chief Steward is far too strict to be behind it, so did you manage to secure a solid connection somewhere in the leadership?”

“Well, I…”

“Just tell me quietly. I’ll keep it to myself. Is it the Outer Hall Master? Or the Iron Sword Squad Leader?”

*The Lesser Family Head sent me here.*

The new martial artist, Jang Childeuk, swallowed the words that had nearly slipped out.

People’s tongues were terribly light. If he told the truth, the rumor would spread before the sun rose tomorrow.

*I can’t cause trouble for the Lesser Family Head!*

When it came to loyalty toward the Jin Family of Taiyuan, Childeuk was no less devoted than any martyr.

He avoided the middle-aged martial artist’s intensely curious gaze and opened his mouth.

“By the way, was this really such a difficult place to get into?”

The middle-aged martial artist looked disappointed at the change of subject and clicked his tongue. Since Childeuk clearly didn’t want to talk about it, there was no point in pressing him further.

“Tsk. You said you’d been with the family for several years, right?”

“That’s right. Although I was a servant.”

“Then how many times did you come to the training hall during those years?”

“Exactly twice.”

“Right? Now, take a good look around.”

“Right now?”

“Or would you rather do it next year?”

Jang Childeuk looked around as instructed.

Beneath the steep cliffs that enclosed the rear of the Jin Family without a single gap, there was a wide-open cavern.

That was the entrance to the training hall, and other than Childeuk and the middle-aged martial artist, there was no one there.

“What do you think?”

“It’s deserted.”

“Right? How many people do you think come here in a day?”

“How many?”

The middle-aged martial artist answered indifferently.

“No one.”

“Pardon?”

“Other than the people who come to change shifts every four shichen, nobody comes here. Ah, there is a servant who delivers meals.”

“But… this is the training hall, isn’t it?”

“It is. But does anyone train here? No. The Third Young Master came in and out a few times after causing trouble, but that’s about it.”

What an absurd thing to say.

Come to think of it, it was called a training hall, but Childeuk had never seen anyone actually training there.

The training ground, on the other hand, was always crawling with martial artists, no matter the season.

“Then why are we guarding this place?”

“It’s a symbol.”

“A symbol?”

“Long ago, Founder Jin Muryang trained here. According to the story, he suddenly attained enlightenment while training on this cliff and unleashed his martial arts, blasting open the base of the cliff with One Strike.”

Jang Childeuk’s mouth fell open.

He remembered hearing the legend of Founder Jin Muryang. Hadn’t he been one of the most renowned masters in the world three hundred years ago?

But how could such a thing be possible with a human body?

“Is, is that really true?”

“It happened hundreds of years ago. What does it matter whether it’s true or false? There’s another fact that’s actually important.”

“…Yes?”

“If you sit around in front of this training hall for a few shichen a day, your monthly pay comes like clockwork. That’s what matters. The only downside is that time passes unbelievably slowly.”

The middle-aged martial artist grinned and patted Childeuk on the shoulder.

“Congratulations. You’ve been assigned to the finest post the martial artists of this family dream of. They call it a cushy post.”

“…”

Childeuk’s face twisted.

It would be one thing if he were old enough to retire at any moment, but he was still in his prime. He had no intention of wasting his time in the training hall with nothing to do.

The middle-aged martial artist, unaware of his thoughts, pulled out a strip of dried meat and began chewing.

“Want one?”

“I’m fine.”

“Why? It’s salty and pretty good. Looking at the sky while chewing jerky makes time pass quickly.”

The middle-aged martial artist leaned against the entrance to the training hall and tilted his head back to look at the sky.

“Well, would you look at that. The sky is so clear. Just looking at it makes my chest feel wide open.”

Jang Childeuk reluctantly glanced upward.

Just as the middle-aged martial artist had said, the weather was clear. A few wispy clouds drifted slowly across the blue sky, along with several black specks.

“What are those?”

“Birds, probably.”

Childeuk’s gaze, which had been fixed blankly on the sky, shifted toward the cliff towering into the heavens. His eyes narrowed.

“What about that thing clinging to the cliff?”

“The cliff? What’s on the cliff?”

“Yes. It’s pretty big.”

“Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…”

Without even looking toward the place Childeuk was pointing, the middle-aged martial artist pulled a small porcelain bottle from his robes.

“It seems too big for a bird.”

“It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.”

“Wow. It really is as big as a person.”

“They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.”

“But, hyung.”

“What? Why do you keep calling me?”

“Do Heavenly Eagles fall, too?”

“What the hell are you talking about?”

The middle-aged martial artist, who had been tilting the bottle toward his mouth, hurriedly looked at the cliff.

At that dizzying height, a massive dot was plummeting rapidly.

“Aaaaaaah!”

Childeuk sounded impressed.

“It really is a spirit creature. Its scream sounds exactly like a person.”

“That’s a person, you lunatic!”

“Whaaa!”

“Move! Move!”

The instant the middle-aged martial artist screamed, a person crashed into the ground amid a shower of stones.

*Boom! Rumble, rumble!*

Rocks and dust burst in every direction. The two men swallowed at the same time.

“D-do you think he’s dead?”

“Try falling from that height. Even the Jade Emperor would die.”

What a calamity to interrupt their peaceful daily routine.

The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown.

“What kind of madman falls from a cliff…”

“He looks young.”

“Does it matter whether he’s young or old? The important thing is that he’s dead.”

“That’s true, but…”

“Go turn him over.”

“M-me?”

“Who else is here besides you and me? Hurry!”

At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body.

He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him.

“Huff, huff.”

The closer he got, the more clearly he could see the body.

Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact.

“May you be reborn in paradise.”

He squeezed his eyes shut and reached out to touch the body.

That was when—

The body sprang upright.

*Crack!*

The world flashed before Childeuk’s eyes, followed by a wave of blinding pain.

He landed hard on his backside, mouth hanging open, unaware that blood was pouring from both nostrils.

“Uh… uhhhh.”

“What the hell just… ugh, ughhh!”

The middle-aged martial artist’s legs gave out, and he collapsed.

“The corpse—the corpse is alive!”

“Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!”

The dirt-covered stranger who had suddenly been written off as dead staggered to his feet.

He looked around with his hair in disarray and blood vessels burst in his eyes, then ground his teeth.

“Fuck, Taecho Village[^2] again?”

* * *

Damn, that hurts.

My head, shoulders, knees, feet, knees, feet… There wasn’t a single place that didn’t ache. Luckily, I had slowed my fall by driving a dagger into the cliff. Otherwise, I might have ended up dead.

Of course, the physique and toughness stats I had steadily raised had helped, too.

“Ow, the back of my head is throbbing.”

When I touched the tender spot on the back of my head, blood came away damply on my fingers.

I tore off a strip of my sleeve and was wiping away the blood when—

“Who are you?!”

“Reveal your identity, you scoundrel!”

Oh, right. Those two older guys were here, too.

One of the two men pointing swords at me looked familiar. What was his name again…

“Jang Childeuk?”

Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror.

“Gasp! How do you know my name?!”

“The jiangshi is talking! It’s bewitching people with its words!”

“…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?”

The middle-aged man with the patchy beard glared at me and shouted.

“You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…”

“Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’”

“That’s right! You’re a jiangshi sent by Taecho Village!”

The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk,

“But where is Taecho Village?”

“I don’t know either.”

“…”

It would have been strange if he did.

I gave up on the conversation and wiped the dirt from my face with my sleeve.

The middle-aged man might not know me, but Childeuk knew my face well. This would be faster.

“Gasp! Third Young Master!”

“Yes. Long time no see.”

“Little brother, the Third Young Master? What in the world are you talking about?”

“The Third Young Master has become a jiangshi!”

“…”

Why was that the conclusion?

[^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire.

[^2]: *Taecho* means “primordial” or “the beginning.”
```
