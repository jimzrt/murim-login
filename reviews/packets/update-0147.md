<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0147.txt",
      "sha256": "d4a88c35f31d12996e8efb4d1b4c4cebba2643494186fd44adfb0bfe0c89b13d",
      "bytes": 14416
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7e1a28b9d1315eb3723f5ff7de9fbb393c085b30f004d794ea561de5d029e335",
      "bytes": 4870
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77fe9696b3da0f32d54cdb08342019060f2d0ea81c945c54debcd2ce396cccf2",
      "bytes": 31273
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d537336c7d9b81a7d62db1d453d0ef503c39c0523a64a8dd1a66ca1b9115f8c5",
      "bytes": 1093
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "95a157983973535a9d4dcb6d3a2f619aa7c076ffaaac61cf1a121b18babf92ef",
      "bytes": 1129
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "1efefaa018662aeedda01a1b7a3a7b23b1c44d8260f8a28533beb87e376539ef",
      "bytes": 1603
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "7177161edc254cc899269fb8909fa60ea8975d001c1bf8f3ecc24c85ec8c5cb2",
      "bytes": 8154
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "554afb13eebaf2d0873de00256392e8051f2c4d960e246a2d5f0fa2abf2b7db7",
      "bytes": 1019
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "71000b0ed6f27b89970b1f178072eb4fdf909249cd66ae46487148dcf2ba2612",
      "bytes": 4621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c2ed9d2391654e19180a87b7f019dede35fa14b77062f39565961f0cc762e40a",
      "bytes": 27321
    }
  ],
  "estimated_tokens": 26031
}
-->

# Durable State Update — Chapter 147

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 147. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 147. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 147,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 147,
    "continuity_sources": [147],
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
    "The City Lord's luncheon attendance requirement has concluded; the Quest target was very satisfied, and Prince Shangshan's Token was obtained as the Quest Reward.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and is expected at the Jin Family's grand banquet in roughly fifteen days.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and Taekyung relaying the proposal to Jin Wikyung; the Seongun Escort Bureau is the proposed base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint, and recognized by Li Feng as his Martial Uncle.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung knows several Huashan martial arts and can use the Zaha Divine Technique with potent Extreme Yang internal energy.",
    "Cheongpung came to Huashan at about age three or four and was not born there; his exact parentage and the truth behind his claim that a crane delivered him to Mae Jonghak remain unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, and has served the prince since infancy; he is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "Cheongpung obtained the Royal Guard Armor Set and decided to remain temporarily at the Jin Family of Taiyuan; he has no martial title yet.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung's side; they will remain at Honghwa Inn until New Year's Day.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao's autograph request three years earlier; Taekyung now promises to obtain Mukyung's autograph for Zhu Bao at the upcoming banquet.",
    "The current Military Commissioner is incompetent, fond of bribes, and directly appointed and dismissed by the Emperor."
  ],
  "continuity_sources": [
    146
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?"
  ],
  "safe_through": 146,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique”; render 근위대 as “royal guard” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 고평문 as “Gopyeong Sect,” 고평지부 as “Gopyeong Branch,” 별호 as “martial title,” 상산왕의 증표 as “Prince Shangshan's Token,” 선황 as “the late Emperor,” 내관 as “palace attendant,” and 고자 contextually as “eunuch” or “castrated.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 큰형     | **eldest brother**                           |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 146
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes; he has no martial title yet, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and learned Huashan martial arts; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 146
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; he formerly served the late Emperor, who ordered him to assist Prince Shangshan, and came to the frontier in something like exile; he remains the power behind the Shanxi Provincial Office, manages the City Lord's luncheon, and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft, candid about his fondness for bribes, and unwaveringly loyal to Prince Shangshan; he remains unashamed and matter-of-fact about having been castrated.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** The late Emperor ordered him to assist Prince Shangshan; Hong Jin has served the prince since infancy and remains loyal to him, while recognizing Taekyung as a young hero of the Jin Family of Taiyuan and increasingly enjoying his company and ruthless political methods.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 145
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 145
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 146
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies; admires Jin Taekyung and seeks to emulate him; has been invited to the Jin Family's grand banquet in fifteen days, where Taekyung promises to obtain Jin Mukyung's autograph for him.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 139
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃147화



진위경은 깊은 탄식을 내뱉었다.

“가문에 돌아오자마자 일을 해야 한다니.”

“며칠 동안 자리를 비우지 않으셨습니까.”

“그거야 피치 못할 사정 때문이지!”

“지금처럼 화내신다고 일이 줄어들지는 않죠.”

“위팽, 나 좀 살려 주게. 이러다가는 정말 과로로 죽고 말걸세.”

간절하고 애처로운 간청에도 위팽은 냉정하게 대답했다.

“일은 끝내고 죽으십쇼. 장례는 성대하게 치러 드리겠습니다.”

“……악귀가 따로 없군. 자네 정말 사람 맞나?”

이미 반나절 앞서 태원진가로 복귀한 진위경을 기다리는 건 산더미처럼 쌓인 일거리였다.

장장 열흘가량이나 자리를 비운 탓에 서탁 위는 물론이고 바닥까지 수백 개의 죽간이 늘어져 있었다.

“이걸 혼자 어떻게 해!”

“하실 수 있습니다. 지금까지 잘하셔 놓고 뭘 새삼스럽게.”

“본가에 이 정도로 사람이 없나? 아니지, 산서성에 기재가 이 정도로 없어?”

“사람 보는 눈을 좀 낮춰야겠다는 생각은 안 하십니까?”

“내 문제라는 말인가?”

“벌써 십여 명이 다녀갔습니다. 제 눈에는 다들 괜찮은 유생(儒生)들이었는데 고작 두 명만 뽑으신 게 실수하신 겁니다.”

“괜찮은 유생은 무슨. 자넨 눈도 없나?”

학문을 익혔다고 무조건 받아들일 수는 없었다.

태원진가는 엄연한 무림 문파. 사서삼경(四書三經)을 얼마나 많이 외웠느냐, 어느 석학의 문하에서 뭘 배웠느냐는 중요하지 않다.

진위경이 원한 인재는 유연한 사고방식을 지닌 실용주의자지 공자 왈, 맹자 왈을 입에 달고 사는 뻣뻣한 유생이 아니다.

“그들 중 두 사람이 유일하게 쓸 만한 자들이었네.”

지금도 그 선택을 후회하지 않는다. 그의 단호한 대답에 위팽이 귀를 후볐다.

“아, 그렇습니까? 그래서 그 두 사람, 지금 어디서 뭘 하고 있습니까?”

“……그, 그건.”

순간 말문이 막힌 진위경을 대신해 위팽이 말을 이었다.

“나흘 동안 꼬박 철야 근무하고 도망쳤잖습니까.”

“도, 도망치긴 누가 도망쳤다고 그러는 건가! 한 명은 어머니가 위독하셔서…….”

“제가 그 친구 사라지고 나서 한번 알아봤습니다. 어머니는 십 년 전에 돌아가셨던데요.”

“……그래?”

“다른 한 명은 잠시 측간에 간다더니 그 길로 내뺐고요. 제 말이 틀립니까?”

“크험, 크허험!”

“주군께서야 무공을 익히셨으니 며칠 밤을 새워도 멀쩡하시겠지만, 그 친구들은 아닙니다. 평생 심법 구결 한 줄 읽어 본 적 없는 양민들이라고요.”

“아, 알고 있네. 그래서 보수를 후하게 챙겨 주잖나.”

“보름만 더 있었으면 그 은자가 유족에게 갔겠죠.”

“…….”

“더 할 말 있으십니까?”

“……없네.”

“없으시면 이제 일 시작하십시오. 다음부터 찾아오는 유생들은 쓸 만하다 싶으면 다 받아들이시고요.”

우울한 얼굴로 고개를 끄덕인 진위경이 죽간 하나를 집어 든 그 순간이었다.

집무실 밖에서 대기 중이던 호위대의 무인 하나가 조심스럽게 들어와 예상치 못한 소식 하나를 전했다.

“누구라고?”

진위경의 물음에 위팽이 대답했다.

“산서성 도지휘동지가 보낸 전령이랍니다.”

“그건 나도 들었네. 한데 도지휘동지라면…… 상산왕의 최측근이자 실세라는 그자?”

“예. 내관 주제에 군부 고위직을 꿰찼다고 말이 많았었죠.”

“그래, 그랬었지.”

진위경 역시 들어 본 기억이 있다. 군부의 꼭대기에 앉아 혼자서 어린 왕을 쥐락펴락한다는 내관에 관한 소문을.

“일면식도 없는데 갑자기 무슨 일일까요?”

“무슨 일이겠나?”

“설마 삼공자 때문에?”

“정황상 그럴 가능성이 매우 농후하지. 우선 전령을 안으로 들이게.”

“예.”

“아, 혹시 모르니 무경이도 부르고.”

“알겠습니다.”

위팽이 수하를 향해 고개를 끄덕인 지 얼마 되지 않아 한 사람이 집무실 안으로 들어섰다.

각을 잰 듯 절도 있는 행동에 가벼운 갑옷 차림.

척 봐도 군 소속으로 짐작되는 그가 바로 홍진이 보낸 전령이었다.

“태원진가의 소가주님 되십니까?”

진위경이 고개를 끄덕였다.

“내가 진 모요. 피차 번잡스러운 서론은 접어 둡시다, 어쩐 일로 오셨소?”

“도지휘동지의 말씀을 전하러 왔습니다.”

“혹, 내 아우와 연관된 일이오?”

“예. 지금 함께 이곳으로 오고 계십니다.”

“함께?”

“그렇습니다. 반 시진 후면 도착하실 겁니다.”

진위경은 그 말을 들으며 가만히 턱을 쓰다듬었다.

사실상 산서성의 이인자 격인 홍진이다. 아무런 이유 없이 움직일 인물은 아니었다.

지금까지 아무런 접점도 없었던 그가 달랑 서신만 보낸 것이라 해도 뜻밖일 터인데, 심지어 직접 오고 있다고 하니 당혹스러울 수밖에.

“선약을 잡은 기억은 없소만.”

위팽이 냉기가 뚝뚝 흐르는 표정으로 한마디를 보탰다.

“도지휘동지가 제아무리 나랏일을 하는 고관(高官)이라고는 하나, 이건 명백히 본가를 무시하는 처사요. 알고 있소?”

“그, 그것이…….”

전령의 이마에 땀방울이 맺혔다.

그도 미약하게나마 군문의 무공을 익힌 몸. 귀검이라 불리는 절정 고수의 눈빛에 가슴이 철렁 내려앉을 수밖에 없었다.

“어떤 용무로 오는 것이오?”

“저, 저는 그저 말씀을 전하라는 명을…….”

“아주 상전이 따로 없군.”

좌불안석이 된 전령을 구원해 준 것은 진위경이었다.

“위팽, 그만하게. 그래서 도지휘동지께서 정확히 뭐라 하시었소?”

“도지휘동지께선 갑작스러운 무례에 미리 사죄의 말씀을 전하라 하셨습니다. 그리고…….”

전령이 품에서 원통 하나를 꺼내 진위경에게 건넸다. 어른 손바닥만 한 원통 안에는 돌돌 말린 하얀 종이가 들어 있었다.

“이게 뭐요?”

“소인도 들은 바가 없습니다. 그저 전해 드리면 알 거라고 하시더군요.”

“흠.”

짐짓 눈살을 찌푸린 진위경이 종이를 펼친 그때, 집무실 문이 열리고 두 번째 손님이 들어왔다.

“부르셨습니까?”

“…….”

“형님?”

한동안 말없이 손에 들린 종이를 바라보던 진위경이 고개를 들었다.

“왔느냐?”

“예. 수련 중에 저를 찾으신다는 말을 듣고…… 한데 어쩐 일로 부르신 겁니까?”

“귀빈이 오기로 해서 말이다. 마중 나갈 채비를 해야겠구나.”

“귀빈, 말입니까?”

“주군. 귀빈이라니요? 마중까지 나갈 필요 있습니까?”

위팽이 인상을 찡그리며 반박했다.

“언질도 없이 오는데 무슨 귀빈입니까? 불청객이지.”

코앞에 전령이 있음에도 거침이 없다. 지금의 태원진가가 산서성에서 차지하는 위치를 생각해 보면 결코 틀린 말은 아니다.

그러나 진위경은 조용히 종이를 건넸다.

“이거 보고 다시 얘기하게.”

“이게 뭡니까?”

“백문이 불여일견.”

“그냥 시원하게 말씀해 주시면 되지 꼭…….”

위팽의 목소리가 점점 줄어들더니 이내 뚝 끊겼다. 눈동자가 쉴 새 없이 움직이며 떨렸다.

종이를 뚫어져라 바라보던 그의 입술이 열린 것은 잠시 후였다.

“귀빈께서 오시는군요.”

“그렇지?”

“예. 맞습니다.”

두 사람의 시선이 아직도 영문을 모르고 멀거니 서 있는 진무경에게로 향했다.

“무경아.”

“이공자.”

“예?”

“너 수련하다가 왔다고 했지.”

“땀 냄새 납니다.”

“수련할 때 땀나는 거야 당연한 거 아닙니까.”

“씻고 와라.”

“당장 씻으십쇼.”

이유를 알 수 없는 두 사람의 반응에 진무경이 답답한 얼굴로 물었다.

“도대체 누가 오기에 이러시는 겁니까?”

진위경과 위팽이 동시에 대답했다.

“큰손.”

“그것도 아주 큰손이죠.”

위팽이 손에 들린 종이를 흔들었다. 그건 천하 어디에서나 사용할 수 있다는 금성전장에서 발행한 천 냥짜리 전표였다.

“이거, 그냥 천 냥 아니다. 은자 천 냥이야.”

은자 천 냥이면 철전으로는 십만 냥이다. 안 그래도 사방에 돈을 퍼붓고 있는 태원진가에게는 가뭄의 단비 같은 거금이었다.

진위경은 실로 오랜만에 둘째 동생에게 정색했다.

“무경아, 이제 씻자.”

“…….”



* * *



마차에서 내리자마자 저절로 한마디가 튀어나왔다.

“와, 시벌…….”

욕을 안 하려야 안 할 수가 없다. 높이 솟은 담벼락 위, 펄럭거리는 천에는 대문짝만한 글씨로 이렇게 쓰여 있었다.



도지휘동지 태원진가 오신 날



부처님 오신 날도 아니고 이게 뭐야.

쪽팔림에 차마 고개를 들지 못하고 있는데, 뒤따라 내린 홍진이 배를 잡고 깔깔 웃었다.

“이야, 생각 이상이네.”

“혹시 저희 큰형님이랑 불알친구라도 됩니까? 도대체 어떻게 하면 이렇게까지 극진한 환대를…….”

“진 공자, 난 불알이 없어요.”

“앗, 아아. 죄송합니다. 정말 죄송합니다.”

엄청난 실수다. 스틱도 없는데 유정란이 남아 있을 리가 있나.

죄책감에 몸부림치는 나를 청풍이 다가와 위로해 주었다.

“은인, 저희 할아버지가 그러셨는데, 눈치 없는 사람은 주위에 친구가 없대요. 하지만 걱정 말아요. 내가 은인의 불알친구가 되어 줄 테니.”

“…….”

필요 없어, 이 새끼야.

애써 욕을 삼키는 내게 홍진이 말했다.

“진 공자, 사람 사이의 관계를 끈끈하게 만들어 주는 게 뭔지 알아요? 바로 재물이야. 금은보화면 귀신도 부린다는데, 산 사람은 오죽하겠어, 안 그래?”

“그럼?”

“선물 준다고 했잖아요. 일종의 뇌물이지 뭐.”

돈이면 귀신도 부린다, 라.

나 역시 어느 정도 동의하는 말이긴 한데 그 대상이 진위경이라는 게 거슬린다.

이미 마음속 깊숙한 곳에서 형이라고 생각하는 그를 뇌물에 넘어간 속물처럼 표현하는 홍진이 곱게 보이지 않는 것이다.

그런 기색이 내 표정에서도 드러나 버렸는지 홍진이 웃음 띤 얼굴로 말했다.

“내 말이 너무 심했나? 하지만 그건 당연한 거예요. 재물 싫어하는 사람이 어디 있겠어?”

“그래도 우리 큰형님입니다. 고작 은자 몇 푼으로 태원진가의 소가주를 구워삶았다고 생각하진 마세요.”

“진 공자…….”

낮은 목소리에 홍진이 눈을 크게 떴다.

“은자 몇 푼이라니. 천 냥이나 줬어.”

“그깟 은자…… 얼마요?”

“은자 천 냥. 철전으로는 십만 냥.”

이제 나도 대충 무림의 물가와 화폐에 대해 감을 잡았다.

특급 호텔이라 할 수 있는 봉황객잔의 별채는 하룻밤에 은자 오십 냥, 양민 네 식구의 일 년 생활비 두 배에 가깝다고 했다.

‘현대 금액으로 따지면 수천만 원.’

은자 천 냥이면 거기서도 20배다. 그러니까 홍진은 수억 원의 돈을 한 번에 툭 던져 준 거다.

“많……네요?”

“많이 줬지. 이번엔 나도 힘 좀 쓴 거야.”

“아니, 그래도 너무 많이 주셨는데.”

“앞으로의 관계를 위해서지. 그리고 지금 태원진가, 지금은 재물이 모이는 것보다 빠지는 게 더 많을걸? 전쟁에서 이기고 적의 영토를 점령한다고 끝나는 게 아니거든.”

“아, 예.”

“이럴 때 주는 도움이 진짜 크게 느껴지는 거지. 나도 뇌물 많이 주고받다 보니까 알게 되더라고. 아, 물론…….”

홍진이 눈을 찡긋하며 말을 이었다.

“진 공자가 아주 마음에 들어서 좀 더 쓴 것도 있고. 내 마음 알지?”

말이 끝나기가 무섭게 엉덩이에서 느껴지는 딱딱한 이물감.

쿡쿡 찔러 오는 감촉에 정신이 번쩍 든다.

‘아니, 이 새끼가 설마?’

맹세컨대 지금까지의 모든 인생을 통틀어 가장 소름 돋는 순간이다.

‘그래, 너 죽고 나 죽자. 전쟁 한 번 더 하자!’

번개 같은 속도로 돌아선 내 눈에 들어온 건 손바닥 절반만 한 크기의 은덩이였다. 저걸 뭐라고 하더라? 은원보?

“자, 이건 내가 주는 용돈.”

아, 맞다. 얘 고자였지.

나는 펄떡거리는 가슴을 진정시키며 대답했다.

“가, 감사합니다.”

“응. 빙당호로 사 먹어요.”

“은인, 사 먹을 때 저도 같이 데려가 주면 안 돼요?”

청풍이 입맛을 다시며 끼어든 그때, 등 뒤에서 익숙한 목소리가 울렸다.

“허허, 숙수들에게 따로 말해 놓을 테니 얼마든지 말만 하시오. 안 그런가, 위팽?”

“빙당호로의 산을 쌓아 놓겠습니다.”

“저놈은 누굽니까? 빙당호로라니, 어린 애도 아니고 무슨.”

누구인지 보지 않아도 알 수 있다. 반가운 웃음과 함께 돌아선 나는 말문이 막히는 장면을 발견했다.

펄럭, 펄럭.

활짝 웃고 있는 진위경과 위팽. 그리고 얼굴이 벌겋게 달아오른 진무경.

세 사람의 손에는 언제 만들었는지 모를 자그마한 천 쪼가리가 바람에 펄럭이고 있었다.



대국 만세! 황상 폐하 만세!

상산왕 전하, 성군이 되시옵소서!



“…….”

“…….”

내가 아까 홍진에게 뭐라고 했더라?

고작 은자 몇 푼으로 대 태원진가의 소가주를 구워삶았다고 생각하지 말라고 했나?

‘시벌, 구워삶기는 개뿔.’

이 정도면 탔다, 탔어.
```

## Final English reading copy

```markdown
# Chapter 147

Jin Wikyung let out a deep sigh.

“I have to start working the moment I return to the family.”

“Were you not away for several days?”

“That was due to circumstances beyond my control!”

“Getting angry like this won’t make the work disappear.”

“Wipeng, save me. At this rate, I’m really going to die of overwork.”

Despite his desperate, pitiful plea, Wipeng answered coldly.

“Finish your work before you die. I’ll give you a grand funeral.”

“……You’re a demon. Are you really human?”

What awaited Jin Wikyung, who had returned to the Jin Family of Taiyuan half a day earlier, was a mountain of work.

Because he had been away for nearly ten days, hundreds of bamboo slips were scattered across not only the writing desk but also the floor.

“How am I supposed to do all this alone?”

“You can do it. You’ve done fine until now, so why are you making such a fuss?”

“Does our family really have so few people? No—are there really so few capable people in all of Shanxi Province?”

“Have you ever considered lowering your standards when it comes to people?”

“Are you saying this is my fault?”

“More than ten people have come and gone already. They all looked like decent scholars to me, but you made the mistake of choosing only two.”

“Decent scholars? Please. Do you have no eye for people?”

They couldn’t simply accept anyone who had studied.

The Jin Family of Taiyuan was, after all, a Murim sect. How much of the Four Books and Three Classics someone had memorized, or what they had learned from which great scholar, wasn’t important.

The kind of talent Jin Wikyung wanted was a practical-minded person with flexible thinking—not a rigid scholar who went around constantly quoting Confucius and Mencius.

“Those two were the only ones among them who were worth using.”

He still didn’t regret that choice. At his firm answer, Wipeng picked at his ear.

“Oh, really? And where are those two now? What are they doing?”

“……Well, that’s…”

When Jin Wikyung was momentarily at a loss for words, Wipeng continued in his place.

“They worked through four straight nights and then ran away.”

“W-who ran away? What are you talking about? One of them had a mother who was gravely ill…”

“I looked into it after that fellow disappeared. His mother died ten years ago.”

“……Really?”

“The other one said he was going to the latrine, then slipped away and never came back. Am I wrong?”

“Cough. Cough-cough!”

“My lord, you’ve trained in martial arts, so you can stay up for several nights and remain perfectly fine. But those men are different. They’re commoners who have never read a single line of a cultivation technique formula in their entire lives.”

“Ah, I know that. That’s why I’m paying them generously.”

“If they had stayed another fifteen days, that silver would have gone to their survivors.”

“……”

“Do you have anything else to say?”

“……No.”

“If you have nothing else to say, start working. From now on, accept any scholars who seem useful when they come looking for work.”

Jin Wikyung nodded gloomily and reached for a bamboo slip.

That was when one of the martial artists from the guard detail waiting outside the office cautiously entered and delivered an unexpected report.

“Who did you say?”

In response to Jin Wikyung’s question, Wipeng answered.

“A messenger sent by the Deputy Military Commissioner of Shanxi Province.”

“I heard that much. But the Deputy Military Commissioner is… that man who’s supposedly Prince Shangshan’s closest aide and the real power behind him?”

“Yes. There used to be plenty of talk about how a palace attendant had managed to secure a high-ranking military post.”

“Right. I remember hearing that.”

Jin Wikyung had heard the rumors about the palace attendant who sat at the top of the military hierarchy and single-handedly kept the young prince under his thumb.

“We’ve never even met him. What could he want all of a sudden?”

“What do you think?”

“Could it be because of the Third Young Master?”

“Given the circumstances, that’s highly likely. Bring the messenger inside first.”

“Yes.”

“Ah, and just in case, call Mukyung as well.”

“Understood.”

Not long after Wipeng nodded to one of his subordinates, a man entered the office.

He moved with measured precision and wore light armor.

Anyone could tell at a glance that he belonged to the military. He was the messenger Hong Jin had sent.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

Jin Wikyung nodded.

“I am Jin Wikyung. Let’s skip the tedious formalities between us. What brings you here?”

“I have come to convey the Deputy Military Commissioner’s words.”

“Is this related to my younger brother?”

“Yes. He is on his way here now, together with the Deputy Military Commissioner.”

“Together?”

“Yes. They should arrive in half a shichen.”

Jin Wikyung silently stroked his chin as he listened.

Hong Jin was effectively the second-most powerful man in Shanxi Province. He wasn’t the sort of person who moved without a reason.

It would have been surprising enough if someone who had never had any connection with them sent nothing but a letter. The fact that he was coming in person made the situation all the more bewildering.

“I don’t recall making an appointment.”

Wipeng added a remark with a face dripping with frost.

“No matter how high-ranking an official the Deputy Military Commissioner is, this is clearly an insult to our family. Are you aware of that?”

“Th-that…”

Sweat gathered on the messenger’s forehead.

He had trained in military martial arts, however slightly. When faced with the gaze of the Peak master known as the Ghost Sword, his heart couldn’t help but sink.

“What business does he have here?”

“I-I was only ordered to deliver his message…”

“He certainly knows how to pull rank.”

The messenger, who had become so nervous he could hardly sit still, was rescued by Jin Wikyung.

“Wipeng, that’s enough. So what exactly did the Deputy Military Commissioner say?”

“He told me to convey his apologies in advance for his sudden rudeness. And…”

The messenger pulled a small cylinder from inside his robes and handed it to Jin Wikyung. Inside the cylinder, which was about the size of an adult’s palm, was a rolled-up sheet of white paper.

“What is this?”

“I haven’t heard anything myself. He merely said that you would understand once it was delivered.”

“Hmm.”

Jin Wikyung deliberately furrowed his brow and unfolded the paper.

At that moment, the office door opened, and a second guest entered.

“Did you call for me?”

“……”

“Older brother?”

Jin Wikyung stared silently at the paper in his hand for a while before raising his head.

“You’re here.”

“Yes. I heard you were looking for me while I was training… What did you call me for?”

“We have an honored guest coming. We need to prepare to go out and greet him.”

“An honored guest?”

“My lord, what do you mean, an honored guest? Do we really need to go out and greet him?”

Wipeng frowned and objected.

“He’s coming without even giving us notice. What kind of honored guest is that? He’s an uninvited guest.”

He showed no restraint despite the messenger standing right in front of him. Considering the position the Jin Family of Taiyuan currently held in Shanxi, it wasn’t an entirely wrong thing to say.

Jin Wikyung quietly handed him the paper.

“Look at this, then we’ll talk again.”

“What is it?”

“Seeing is believing.”

“You could simply tell me instead of making such a fuss…”

Wipeng’s voice gradually grew quieter before cutting off completely. His eyes trembled as they darted back and forth.

A moment later, his lips parted.

“An honored guest is coming.”

“Right?”

“Yes. Exactly.”

The two men turned their gazes toward Jin Mukyung, who was still standing there with no idea what was going on.

“Mukyung.”

“Second Young Master.”

“Yes?”

“You said you came straight from training, right?”

“You smell like sweat.”

“It’s only natural to sweat when you train.”

“Go wash.”

“Wash immediately.”

Unable to understand the reason for their reactions, Jin Mukyung asked with a frustrated expression,

“Who on earth is coming to make you act like this?”

Jin Wikyung and Wipeng answered at the same time.

“A big spender.”

“And an extremely big one at that.”

Wipeng waved the paper in his hand. It was a thousand-nyang bank draft issued by the Golden Star Exchange, valid anywhere under heaven.

“This isn’t just a thousand nyang. It’s a thousand nyang of silver.”

A thousand silver nyang was worth one hundred thousand nyang in iron coins. To the Jin Family of Taiyuan, which was already pouring money out in every direction, it was a fortune like rain after a drought.

For the first time in a long while, Jin Wikyung gave his younger brother a stern look.

“Mukyung, let’s go wash up.”

“……”

* * *

The moment I got out of the carriage, a word slipped out on its own.

“Wow, fuck…”

There was no way I could stop myself from swearing. Atop the towering wall, a fluttering cloth banner displayed enormous letters that read:



**The Day the Deputy Military Commissioner Came to the Jin Family of Taiyuan**

*This isn’t even Buddha’s Birthday. What the hell is this?*

I was too embarrassed to lift my head when Hong Jin climbed down behind me and burst out laughing, clutching his stomach.

“Wow. This is beyond what I expected.”

“Are you perhaps childhood friends with my eldest brother? How else could he give you such an enthusiastic welcome…?”

“Young Master Jin, I don’t have balls.”

“Ah—oh. I’m sorry. I’m really sorry.”

That was a tremendous blunder. Without a stick, there was no way any fertilized eggs would be left behind.

As I writhed under the weight of my guilt, Cheongpung approached and comforted me.

“Benefactor, my grandfather used to say that people who don’t know how to read the room have no friends around them. But don’t worry. I’ll be your ball friend.”

“……”

*I don’t need one, you bastard.*

As I desperately swallowed my curses, Hong Jin spoke to me.

“Young Master Jin, do you know what makes relationships between people strong? Wealth. They say gold and silver can make even ghosts work for you. Living people should be even easier, don’t you think?”

“And?”

“I told you I’d give him a present. It’s basically a bribe.”

*Money can make even ghosts work for you.*

I agreed with that to some extent, but I didn’t like the fact that the person in question was Jin Wikyung.

I already thought of him as my older brother deep down. I didn’t appreciate Hong Jin making him out to be some materialistic opportunist who could be bought with a bribe.

Perhaps that displeasure showed on my face, because Hong Jin smiled and said,

“Was that too harsh? But it’s only natural. Who doesn’t like wealth?”

“He’s still my eldest brother. Don’t think you’ve won over the Lesser Family Head of the Jin Family of Taiyuan with a measly few silver nyang.”

“Young Master Jin…”

Hong Jin’s eyes widened at my low voice.

“A few silver nyang? I gave him a thousand nyang.”

“Just a few silver… How much?”

“A thousand silver nyang. That’s one hundred thousand nyang in iron coins.”

I had finally gotten a rough sense of prices and currency in the Murim.

The private suite at the Phoenix Inn, which could be considered a luxury hotel, cost fifty silver nyang per night. That was said to be close to twice the annual living expenses of a family of four commoners.

*In modern currency, that would be tens of millions of won.*

A thousand silver nyang was twenty times that. In other words, Hong Jin had casually tossed around several hundred million won in one go.

“That’s… a lot, isn’t it?”

“A lot, yes. I put in some effort this time.”

“Still, that’s far too much.”

“It’s for the sake of our future relationship. And right now, the Jin Family of Taiyuan is probably losing money faster than it’s bringing money in. Winning a war and occupying the enemy’s territory isn’t the end of it.”

“Ah, yes.”

“The assistance you give at times like this feels much greater. I learned that after giving and receiving so many bribes myself. Ah, of course…”

Hong Jin continued with a wink.

“I did spend a little extra because I took a particular liking to Young Master Jin. You understand my feelings, right?”

The moment he finished speaking, I felt a hard foreign object against my butt.

The sensation poking me repeatedly snapped me fully awake.

*No way. Is this bastard seriously…?*

I swear, in my entire life, this was the most spine-chilling moment I had ever experienced.

*Fine, if you’re going down, I’m going down too. Let’s have another war!*

I spun around at lightning speed.

What met my eyes was a silver lump about half the size of my palm. What did they call those again? A silver yuanbao?

“Here. Pocket money from me.”

*Oh, right. He was a eunuch.*

I calmed my pounding heart and answered.

“Th-thank you.”

“Sure. Go buy some candied hawthorn skewers.[^1]”

“Benefactor, could you take me with you when you go buy them?”

Cheongpung joined in, smacking his lips.

Just then, a familiar voice rang out from behind us.

“Heh heh. I’ll tell the cooks separately, so order as much as you like. Right, Wipeng?”

“We’ll build a mountain of candied hawthorn skewers.”

“Who is that fellow? Candied hawthorn skewers? He isn’t even a child, so what’s this about?”

I didn’t need to look to know who it was.

I turned around with a happy smile, only to find a scene that left me speechless.

*Flutter. Flutter.*

Jin Wikyung was smiling broadly. So was Wipeng. Jin Mukyung’s face was bright red.

In the hands of all three men, tiny scraps of cloth fluttered in the wind. I had no idea when they had made them.



> **Long live the Great Nation! Long live His Imperial Majesty the Emperor!**
>
> **His Highness Prince Shangshan, may you become a sage king!**

“……”

“……”

*What had I said to Hong Jin earlier?*

*Had I told him not to think he’d won over the Lesser Family Head of the mighty Jin Family of Taiyuan with a mere few silver nyang?*

*Fuck, “won him over” my ass.*

At this point, he was burned—burned to a crisp.

[^1]: Candied hawthorn skewers are a traditional snack of fruit coated in hardened sugar.
```
