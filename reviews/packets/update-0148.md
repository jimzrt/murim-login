<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0148.txt",
      "sha256": "8b5022e1bc1e114b12e9e63e5f6948d91548ca581f172e9b377a0b606f0939cc",
      "bytes": 13450
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2171aaedb334760028f654717dc162fff0027f4aab94b81563cf634a4e468733",
      "bytes": 5201
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1d6d0a2876b945b62b0bfc8fdb179a1ef78bd736329598b1a9aa23e1250948fe",
      "bytes": 32008
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d5824d9392f8acb1e031d30f92f61de03c54209bfa1ad0c20938772c83890575",
      "bytes": 1093
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "cc533870bf158ef7b64f53a618ac270f4a002ad70fb98b73787fbf3ca4149272",
      "bytes": 1129
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "01ed1c170e424267d58243d09d00cc419127b69f9db8f7eace2a0f6ce7a91e26",
      "bytes": 1603
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "ef11eced589e77f1a3a791d9b1e6cb130cbeab0e9c1d3543736fe3849e3fa9ae",
      "bytes": 8154
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "3406c92a0a3420a2e120c7fcd6782a6b784651189a71796c67e92dff198a59f2",
      "bytes": 468
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "a6044747e4bb056a7a84ccf476819c14da58e582f940a86ce1b08fd27f3d39bc",
      "bytes": 1356
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "5e28baf9d5fa27c44e49bea175ca258d8db8c27c08c342ffda235e48a18f7d4d",
      "bytes": 4621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "667e9e47ca7032fd78739440531cb3257d5d6de11763318cfad83a3b61fdcee7",
      "bytes": 27687
    }
  ],
  "estimated_tokens": 26185
}
-->

# Durable State Update — Chapter 148

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 148. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 148. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 148,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 148,
    "continuity_sources": [148],
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
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint; he knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, and has no martial title yet.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung came to Huashan at about age three or four and was not born there; his exact parentage and the truth behind his claim that a crane delivered him to Mae Jonghak remain unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung's side; they will remain at Honghwa Inn until New Year's Day.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao's autograph request three years earlier; Taekyung now promises to obtain Mukyung's autograph for Zhu Bao at the upcoming banquet.",
    "The current Military Commissioner is incompetent, fond of bribes, and directly appointed and dismissed by the Emperor.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away and is responsible for a large administrative workload; he prefers practical people with flexible thinking over rigid scholars.",
    "Hong Jin gave Jin Wikyung one thousand silver nyang, and the Jin Family responded with an extravagant pro-imperial welcome."
  ],
  "continuity_sources": [
    147
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
  "safe_through": 147,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique”; render 근위대 as “royal guard” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 고평문 as “Gopyeong Sect,” 고평지부 as “Gopyeong Branch,” 별호 as “martial title,” 상산왕의 증표 as “Prince Shangshan's Token,” 선황 as “the late Emperor,” 내관 as “palace attendant,” 고자 as “eunuch,” 금성전장 as “Golden Star Exchange,” 전표 as “bank draft,” 은자 as “silver nyang,” 철전 as “iron coins,” 은원보 as “silver yuanbao,” 사서삼경 as “Four Books and Three Classics,” 대국 as “Great Nation,” and 성군 as “sage king.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 극양                        | **Extreme Yang**      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 147
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes; he has no martial title yet, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and learned Huashan martial arts; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 147
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; he formerly served the late Emperor, who ordered him to assist Prince Shangshan, and came to the frontier in something like exile; he remains the power behind the Shanxi Provincial Office, manages the City Lord's luncheon, and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft, candid about his fondness for bribes, and unwaveringly loyal to Prince Shangshan; he remains unashamed and matter-of-fact about having been castrated.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** The late Emperor ordered him to assist Prince Shangshan; Hong Jin has served the prince since infancy and remains loyal to him, while recognizing Taekyung as a young hero of the Jin Family of Taiyuan and increasingly enjoying his company and ruthless political methods.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 147
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 147
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 144
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 144
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 147
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃148화



십만 냥이라는 거금이 따뜻하게 덥혀 놓은 분위기 속, 진위경과 홍진이 인사를 주고받았다.

“태원진가의 진위경이라 합니다. 말로만 듣던 도지휘동지를 뵙게 되어 기쁘기 한량없습니다.”

“대태원진가의 소가주께서 이리 환대해 주시니 몸 둘 바를 모르겠네요. 앞으로는 편하게 홍 동지라고 불러 주세요.”

“그래도 벼슬하시는 분께 그럴 수야 있습니까.”

“아이, 너무 딱딱하시다. 편하게 부르시라니까.”

“하하, 그럼 그럴까요, 홍 동지?”

갑자기 분위기 공산주의 뭔데.

여기가 평양인지 무림인지 고민하고 있을 때, 통성명을 끝마친 진위경의 시선이 이쪽을 향했다.

“음. 태경이 왔느냐?”

“예.”

평소와는 다른 묵직한 목소리에 눈치껏 공손히 대답했다.

아무래도 외부인이 보는 앞에서 평소처럼 굴었다가는 진위경 개인의 위신은 물론이고 가문 전체가 망신임을 알고 있는 것 같다.

“그래, 전하께 인사는 잘 드렸고?”

인사 정도가 아니라 단독 팬 사인회도 하고 왔지.

홍진이 웃으며 내 어깨를 톡톡 두드렸다.

“전하께서 아주 기뻐하셨어요. 평소에 여기 진 공자를 너무 보고 싶어 하셨거든요.”

“아, 그렇습니까?”

“네. 얼마나 좋아하시던지 도무지 놔줄 생각을 안 하시더라니까요.”

“으허허, 우리 막내…… 아니. 제 아우가 마음에 쏙 드신 모양이군요.”

“그럴 만도 하죠. 얼굴 잘생겼지, 키 크고 몸 좋지. 무공도 강한 데다 성격도 아주 서글서글하니 싫어할 사람이 어디 있겠어요?”

“으흠, 제 입으로 이런 말 하긴 뭐 하지만, 사실 태경이가 대단한 인재이긴 합니다. 본가가 아니라 오대세가 같은 곳에서 태어났으면 천하제일인이 되었어도 이상하지 않아요.”

무게 잡는 것도 잊고 신이 나서 떠들어 대는 진위경의 모습에 홍진이 얼굴을 굳혔다.

“천하제일이요? 진 소가주님. 농담이 너무 심하시다.”

“네? 그게 무슨.”

“진 공자가 천하제일인이 될 재목이라니요. 아무리 제가 무림과 연이 없다고 해도 그렇지, 너무 우습게 보시는 거 아녜요?”

“……커흠.”

순간 싸해진 분위기 속에 진위경이 불편한 헛기침을 내뱉었다. 그때 홍진이 재깍 말을 이었다.

“진 공자 정도라면 고금제일인도 될 수 있죠.”

“……!”

“미리 축하드려요, 소가주님. 태원진가에서 고금제일인이 나오다니, 산서성의 홍복이네요.”

진위경이 감격에 찬 얼굴로 외쳤다.

“홍 동지!”

“진 소가주님!”

“…….”

황궁에서 20년을 살았다더니, 과연 혓바닥 놀리는 솜씨가 보통이 아니다.

나는 영혼의 단짝을 만나기라도 한 것처럼 기뻐하는 진위경을 보며 혀를 내둘렀다.

“안 되겠습니다. 여기서 이럴 게 아니라 제가 자리를 마련해 뒀으니 술이라도 한잔…….”

“어쩌죠? 제가 술은 잘 못 먹어서.”

“아, 이리 안타까울 수가.”

“없어서 못 먹어요.”

“홍 동지!”

“진 소가주님!”

“…….”

“…….”

쿵짝 잘 맞는 거 봐라.

두 사람이 껄껄 웃으며 어깨동무를 하고 사라지자 위팽이 황당하다는 얼굴로 나를 바라봤다.

“저자가 정말 도지휘동지가 맞습니까?”

“안타깝지만 사실이에요.”

“내관 출신이라고는 들었지만 저렇게 경박스러울 줄은.”

글쎄, 그럼 거기에 맞장구까지 다 쳐 준 무인 출신인 진위경은 뭐가 되나.

아까부터 썩은 표정이던 진무경이 입을 열었다.

“원래 저런 작자입니다. 지난번에는 은근슬쩍 제 어깨를 쓰다듬더군요. 팔을 부러트리려다가 간신히 참았습니다.”

손에 들고 있던 천을 쫙쫙 찢어 땅바닥에 내팽개친 그가 한결 후련해진 표정으로 말했다.

“그럼 전 중요한 볼일이 있어서 이만.”

“볼일은 무슨. 또 수련이겠지 뭐.”

“무인에게 있어 수련보다 중요한 일이 있나?”

“……없지.”

할 말 없게 만드는군.

말문이 막혀 입맛만 다시던 그때, 또랑또랑하고 맑은 목소리가 울려 퍼졌다.

“우와, 저희 할아버지가 항상 하시는 말씀이랑 똑같아요.”

순간 위팽과 진무경의 시선이 청풍을 송곳처럼 찔렀다.

양민들이 볼 때야 조금 독특한 분위기의 청년, 딱 그 정도지만 고수들에겐 다르다.

두 사람의 눈썹이 위로 솟구치자 청풍이 당황한 얼굴로 나를 돌아봤다.

“어, 은인. 제가 무슨 잘못이라도 했나요?”

“잘못은 무슨. 그냥 신기해서 그런 거예요. 그렇죠, 두 분?”

두 사람은 청풍에게 시선을 고정시킨 채 고개만 끄덕였다.

새파랗게 젊은 절정 고수. 그들로서는 난데없이 튀어나온 청풍의 정체가 궁금할 법도 했다.

“이참에 서로 통성명이라도 하시죠. 이쪽은 청풍.”

내 말이 끝나기가 무섭게 청풍이 고개를 꾸벅 숙였다.

“안녕하세요, 청풍입니다! 산서에 온 지는 며칠밖에 안 됐고요. 그전에는 하남에 있었고 또…….”

이거 어디서 굴러먹다 온 놈이야? 두 사람의 얼굴엔 딱 저렇게 쓰여 있다.

예상했던 바다. 나는 청풍의 정체를 간단명료하게 설명했다.

“검성의 제잡니다.”

“……!”

“……!”

검성 매종학의 이름은 무림인들에게 있어 확실히 치트키나 다름없다.

두 사람이 경악에 찬 얼굴로 입을 딱 벌리고 말을 잇지 못하자 청풍이 조심스럽게 물었다.

“저어, 그런데 두 분 중 누가 진천검이시죠?”

아직 충격에서 빠져나오지 못한 진무경이 더듬더듬 대답했다.

“내, 내가 진천검이오. 한데 정말 검성 매종학 대협의……?”

“네. 저희 할아버지세요.”

“헉!”

화염신장의 비급을 봤을 때보다 몇 배는 놀란 표정이다.

이미 수십 년 전 은거한 것으로 알려진 초절정 고수의 제자, 그것도 손자라고 하는 젊은이가 툭 튀어나왔으니 그럴 만도 했다.

“이럴 수가…….”

“검성의 후인이라니.”

놀라움을 금치 못하는 두 사람을 번갈아 보던 청풍이 해맑게 웃었다.

“저도 하산하기 전까지는 몰랐네요.”

“소, 소협. 혹시 매 대협께서도 하산을……?”

물어보는 목소리에는 기대와 흥분이 한껏 담겨 있었다.

두 사람 모두 일평생 검을 수련해 온 검객. 매종학은 검성이라는 별호를 얻을 정도로 검도(劍道)의 경지를 이룩한 사람이니 그들에게 있어 신이나 다름없는 존재였다.

그러나 청풍은 대답은 두 사람의 기대를 산산조각 냈다.

“아뇨, 저만 몰래 도망쳐 나왔어요. 만나고 싶은 분들이 있어서.”

“아아.”

“그럴 수가…….”

“근데 그건 그렇고…….”

안타까워하는 두 사람을 바라보던 청풍이 재차 입을 열었다.

그의 반짝거리는 눈빛은 아까 전부터 진무경에게 고정되어 있었다.

“정말 진천검 진무경 소협이신가요? 십봉룡(十鳳龍)의 그분?”

“맞소, 내가 진무경이오.”

“와, 드디어 찾았다!”

“……음?”

“제가 그쪽을 엄청 찾아 헤맸거든요. 하남의 천무학관에서부터 여기까지.”

뭐야, 저 녀석이 찾고 있던 사람이 진무경이었어?

위팽은 물론이고 당사자인 진무경도 어리둥절한 표정으로 물었다.

“날 말이오?”

“네. 마침 가깝기도 하고, 첫 번째 시작으로 나쁘지 않겠다 싶어서요.”

“첫 번째라니. 그게 무슨 말이오?”

“비무행(比武行).”

청풍이 잔잔하게 웃었다. 그건 지금까지 보아 왔던 해맑고 순수한 웃음과는 전혀 다른 종류의 것이었다.

“하산하면서 결심했지요. 십봉룡을 모두 꺾기 전에는 돌아가지 않겠다고.”

“……!”

“할아버지께서 그러셨어요. 무인에게는 대화가 필요 없다. 오직 무(武)로 겨룰 뿐이다.”

스으으.

그 순간, 나는 뜨거운 열기를 느꼈다. 어느새 솟구친 자줏빛 광염(光焰)이 청풍의 전신에서 피어오르고 있었다.

이미 한 번 본 적 있는 광경이다.

‘자하신공.’

극양의 기운이 냉기를 불살랐다. 땅이 녹고 흙이 그을렸다. 청풍이 웃음이 사라진 얼굴로 입을 열었다.

“자리를 옮길까요?”

“그럴 필요 있나?”

진무경의 말이 이어졌다.

“검을 뽑아.”



* * *



진무경은 길게 숨을 내뱉었다. 빠르게 뛰던 심장이 천천히 속도를 늦춘다. 전투에서 중요한 것은 호흡이다. 이제야 비로소 검을 뽑을 준비를 갖췄다.

그는 검파에 손을 올리며 한 사람의 이름을 떠올렸다.

‘검성 매종학.’

검을 처음 쥔 날부터 단 하루도 그 이름을 잊은 적이 없었다.

검의 궁극에 다다랐다는, 혹은 그 너머의 경지에 이르렀다는 전설적인 검객.

모두가 검성을 추앙했지만 진무경은 달랐다.

‘언젠가 그를 꺾고 말겠다.’

누군가 들었다면 코웃음을 쳤을 일이다. 미친놈이라며 손가락질했을 것이다.

진무경이 제아무리 천재라 한들 검성이라는 이름에는 닿을 수 없다. 매종학이 검성이라 불리기 시작한 이래, 그 누구도 그를 넘어서지 못했으니까.

검성 매종학은 이미 수십 년 전 정파 무림의 새로운 역사를 썼고, 신화의 주인공이 되었다.

‘상관없어. 이건 내 목표니까.’

만용이 아니라 목표다.

지금껏 검을 수련하며 매일같이 뼈와 가슴에 새겨 온 목표.

그리고 이 순간, 검성 매종학의 모든 것을 물려받은 한 사람이 눈앞에 있다.

“할아버지께서 그러셨죠. 너는 십봉룡에 비하면 아무것도 아니다. 자만하지 말아라.”

청풍이 천천히 발을 내디뎠다. 허리춤에는 아무렇게나 매인 청강검 한 자루가 대롱거렸고, 발걸음은 산책이라도 나온 것처럼 가벼웠다.

그러나…….

‘빈틈이 없다.’

허술하기 짝이 없는데 도무지 언제, 어떻게 상대를 공격해야 할지 모르겠다.

진무경은 바짝 마른 입술을 핥았다.

“난 그분을 만나 본 적도 없는데…… 과찬을 하셨군.”

“아니에요. 솔직히 살짝 놀랐는걸요. 이건 진심이에요.”

진무경 역시 지금 청풍이 하는 말들이 모두 진심이라는 사실을 안다. 그래서 더 기분이 묘했다.

‘살짝, 이라고.’

검을 수련한 지 어느덧 이십여 년이 지났다. 재능과 노력을 바탕으로 이 자리에 올랐다.

세인들은 자신을 천재라고 불렀고, 진천검이라는 별호를 붙여 주었으며 십봉룡이라 칭했다.

단 한 번도 그런 허명(虛名)에 취한 적이 없다고 생각했는데…….

‘나도 아직 한참 멀었군.’

어느새 자신을 우러러보는 사람들의 시선에 익숙해져 있었던 모양이다.

얼마 전 풍양에게 당한 상처가 다시 욱신거리는 듯했다.

“그거 아시오?”

“뭘요?”

“당신이 강하다는 것.”

“사실 얼마 전까지 확신하지 못했어요. 하지만 이제는 알겠네요.”

“나를 만나서?”

“네. 진 소협을 만나서. 십봉룡이 어느 정도인지 알게 됐으니까요.”

“그렇소?”

진무경이 피식 웃었다.

재미있는 놈이다. 이미 구파일방의 장로에 버금가는 무공, 혹은 그 이상이면서도 때 묻지 않은 순수함. 솔직함.

무인이지만 무림에는 어울리지 않는 놈이다.

‘내가 아는 누구랑은 정반대로군.’

문득 한 사람이 떠오른다.

무림 어디에 던져 놔도 어떻게든 살아남을 것 같은 놈, 동시에 가장 무인답지 않게 싸우는 놈이.

“나이가 어떻게 되시오?”

“올해로 약관입니다.”

“마침 나이도 같군. 우연인가? 아니면 인연?”

“네?”

진무경은 대답 대신에 고개를 저었다.

사실 이 비무의 결과는 이미 알고 있다. 청풍의 전신에서 넘실거리는 자하신공의 기운이 그만큼 압도적이었으니까.

이 정도의 고수를 상대로 모든 기량을 펼치지 못하는 것이 아쉬울 뿐이다.

‘이럴 때 저 녀석이라면 어떻게 했을까?’

진무경은 자신의 사고뭉치 동생을 흘끗 바라봤다. 놈은 악동 같은 웃음과 함께 입을 벙긋거리고 있었다.

넌. 좆. 됐. 다.

이런 쳐 죽일 놈을 봤나. 허탈하게 웃은 진무경이 검파에 손을 올렸다. 단전에서 끓어오른 공력이 사지백해로 뻗어 나간다.

청풍이 진무경의 검을 바라보며 입을 열었다.

“할아버지께서 그런 말씀도 해 주셨어요. 비무에는 기수식 따위 필요 없다.”

“동감이오.”

다음 순간.

거대한 굉음과 함께 자줏빛 광염과 은빛 검기가 격돌했다.
```

## Final English reading copy

```markdown
# Chapter 148

In the atmosphere warmed by the enormous sum of a hundred thousand nyang, Jin Wikyung and Hong Jin exchanged greetings.

“I am Jin Wikyung of the Jin Family of Taiyuan. It is an immense pleasure to meet the Deputy Military Commissioner I’ve heard so much about.”

“Being so warmly welcomed by the Lesser Family Head of the great Jin Family of Taiyuan leaves me at a loss. From now on, please just call me Comrade Hong.”

“Even so, how could I address an official that casually?”

“Come now, you’re being too stiff. I said to call me casually.”

“Ha-ha. Then shall I, Comrade Hong?”

What was with the sudden communist atmosphere?

As I wondered whether I was in Pyongyang or the Murim, Jin Wikyung finished exchanging introductions and turned his gaze toward me.

“Hmm. Taekyung, you’re here?”

“Yes.”

His voice was heavier than usual, so I answered politely and read the room.

Apparently, he understood that acting as he normally did in front of outsiders would not only damage his personal dignity but also humiliate the entire family.

“So, did you greet His Highness properly?”

*Properly? I didn’t just greet him. I even held a private autograph session.*

Hong Jin smiled and patted my shoulder.

“His Highness was delighted. He’d always wanted to meet Young Master Jin here.”

“Oh, is that so?”

“Yes. He was so happy that he had no intention of letting him go.”

“Uhehehe. It seems our youngest—no. It seems His Highness has taken quite a liking to my younger brother.”

“I can see why. He’s handsome, tall, and well-built. He’s strong in martial arts, and he has such an easygoing personality. Who could dislike him?”

“Ehem. It feels strange to say this myself, but Taekyung really is an extraordinary talent. If he had been born somewhere like the Five Great Families instead of our family, it wouldn’t be strange if he became the greatest under heaven.”

Hong Jin’s expression hardened as Jin Wikyung got carried away, chattering excitedly and forgetting all about maintaining his dignity.

“The greatest under heaven? Lesser Family Head Jin, that’s too much of a joke.”

“Pardon? What do you mean?”

“You’re saying Young Master Jin has what it takes to become the greatest under heaven? Even if I have no connection to the Murim, surely you aren’t making light of me.”

“……Ahem.”

As the atmosphere instantly turned cold, Jin Wikyung gave an uncomfortable cough. Hong Jin immediately continued.

“Someone like Young Master Jin could become the greatest of all time.”

“……!”

“Allow me to congratulate you in advance, Lesser Family Head. For the greatest of all time to come from the Jin Family of Taiyuan—what a blessing for Shanxi Province.”

Jin Wikyung cried out with a deeply moved expression.

“Comrade Hong!”

“Lesser Family Head Jin!”

“……”

They say Hong Jin lived in the imperial palace for twenty years. His skill with his tongue certainly wasn’t ordinary.

I clicked my tongue as I watched Jin Wikyung rejoice as though he had found his soulmate.

“This won’t do. There’s no point staying here. I’ve already arranged a place, so why don’t we have a drink?”

“What should I do? I’m not very good with alcohol.”

“Ah, what a shame.”

“The only time I can’t drink is when there’s none to be had.”

“Comrade Hong!”

“Lesser Family Head Jin!”

“……”

“……”

Look at how perfectly they clicked together.

When the two men disappeared, laughing loudly with their arms around each other’s shoulders, Wipeng stared at me with an utterly dumbfounded expression.

“Is that man really the Deputy Military Commissioner?”

“Unfortunately, yes.”

“I heard he was a former palace attendant, but I didn’t know he’d be so frivolous.”

Well, then what did that make Jin Wikyung, a martial artist who had played along with every bit of it?

Jin Mukyung, who had been wearing a sour expression for some time, finally spoke.

“That’s just the kind of man he is. Last time, he subtly stroked my shoulder. I barely stopped myself from breaking his arm.”

He ripped the cloth in his hands into strips and threw them onto the ground, then spoke with a much more relieved expression.

“Then I have important business, so I’ll be leaving.”

“What business? Training again, I assume.”

“Is there anything more important to a martial artist than training?”

“……No.”

That left me with nothing to say.

As I stood there at a loss, merely smacking my lips, a clear, ringing voice rang out.

“Wow, that’s exactly what my grandfather always says.”

Wipeng and Jin Mukyung’s gazes pierced Cheongpung like awls.

To ordinary people, Cheongpung was merely a young man with a slightly unusual air about him. To masters, however, he was something else entirely.

When both men’s eyebrows shot upward, Cheongpung turned to me with a flustered expression.

“Uh, Benefactor. Did I do something wrong?”

“What do you mean, wrong? They just found it interesting. Right, gentlemen?”

Neither man took his eyes off Cheongpung. They merely nodded.

An extraordinarily young Peak master. It was only natural that they would be curious about the identity of this Cheongpung who had suddenly appeared out of nowhere.

“Since we’re here, why don’t you introduce yourselves? This is Cheongpung.”

Before I had even finished speaking, Cheongpung gave a deep bow.

“Hello, I’m Cheongpung! I’ve only been in Shanxi for a few days. Before that, I was in Henan, and before that…”

*Where did this guy crawl out of?*

The question was written plainly across both men’s faces.

Just as I expected. I explained Cheongpung’s identity simply and clearly.

“He’s the Sword Saint’s disciple.”

“……!”

“……!”

The name of Sword Saint Mae Jonghak was practically an instant cheat code among martial artists.

When the two men stared at Cheongpung in shock, mouths hanging open and unable to speak, he asked cautiously,

“Um, which of you is the Heaven Shaking Sword?”

Jin Mukyung, who still hadn’t recovered from the shock, stammered out a reply.

“I-I’m the Heaven Shaking Sword. But are you really the Sword Saint Mae Jonghak’s…?”

“Yes. He’s my grandfather.”

“Gasp!”

He looked several times more shocked than when he had seen the Flame Divine Palm martial arts manual.

A young man claiming to be the disciple—and grandson—of a Supreme Peak master who was known to have gone into seclusion decades ago had suddenly appeared before them. Their reaction was understandable.

“This can’t be…”

“He’s the Sword Saint’s successor…”

Cheongpung looked back and forth between the two astonished men, then smiled brightly.

“I didn’t know either until I came down the mountain.”

“Y-Young Hero. Did Great Hero Mae also descend the mountain…?”

His voice was filled with expectation and excitement.

Both men had trained in swordsmanship their entire lives. To them, Mae Jonghak was practically a god—a man who had reached such a level in the Way of the Sword that he had earned the martial title of Sword Saint.

But Cheongpung’s answer shattered their expectations.

“No. I just snuck out by myself. There were people I wanted to meet.”

“Ah…”

“How unfortunate…”

“But putting that aside…”

Cheongpung looked at the two crestfallen men before speaking again.

His bright eyes had been fixed on Jin Mukyung for some time.

“Are you really Young Hero Jin Mukyung, the one from the Ten Dragons and Phoenixes?”

“That’s right. I’m Jin Mukyung.”

“Wow, I finally found you!”

“……Hmm?”

“I searched everywhere for you. From Heaven’s Gate Temple in Henan all the way here.”

*What? The person that guy had been looking for was Jin Mukyung?*

Wipeng, as well as Jin Mukyung himself, asked with bewildered expressions,

“You were looking for me?”

“Yes. Since you were nearby, I thought you’d be a decent place to start.”

“A first? What does that mean?”

“A dueling tour.”

Cheongpung smiled softly. It was completely different from the bright, innocent smile I had seen from him until now.

“I decided it while coming down the mountain. I won’t return until I’ve defeated all the Ten Dragons and Phoenixes.”

“……!”

“My grandfather told me this: A martial artist has no need for conversation. We settle things through martial arts alone.”

Sssss.

At that moment, I felt a wave of heat. Violet light-flames had risen around Cheongpung’s entire body, surging upward.

I had already seen this once before.

*The Zaha Divine Technique.*

The Extreme Yang qi burned the cold away. The earth melted, and the soil scorched. Cheongpung opened his mouth with all traces of his smile gone.

“Shall we move somewhere else?”

“Is there any need?”

Jin Mukyung continued,

“Draw your sword.”

* * *

Jin Mukyung let out a long breath. His rapidly beating heart slowly began to settle. Breathing was important in battle. Only now was he finally ready to draw his sword.

As he placed a hand on the hilt, he thought of one man’s name.

*Sword Saint Mae Jonghak.*

Not once had he forgotten that name since the day he first held a sword.

A legendary swordsman who was said to have reached the ultimate realm of the sword—or perhaps a realm beyond it.

Everyone revered the Sword Saint, but Jin Mukyung was different.

*Someday, I’ll defeat him.*

If anyone had heard him say that, they would have snorted. They would have pointed at him and called him crazy.

No matter how talented Jin Mukyung was, he could never touch the Sword Saint’s level. Ever since Mae Jonghak had begun to be called the Sword Saint, no one had surpassed him.

Sword Saint Mae Jonghak had written a new chapter in the history of the orthodox Murim decades ago and become the protagonist of a legend.

*It doesn’t matter. This is my goal.*

It wasn’t reckless arrogance. It was a goal.

A goal he had etched into his bones and heart every day as he trained with his sword.

And at this very moment, someone who had inherited everything from Sword Saint Mae Jonghak stood before him.

“My grandfather used to tell me this. ‘Compared to the Ten Dragons and Phoenixes, you are nothing. Don’t become arrogant.’”

Cheongpung slowly stepped forward. A single blue-steel sword dangled from his waist, tied on haphazardly, and his footsteps were as light as though he had come out for a stroll.

But…

*There are no openings.*

He looked utterly careless, yet Jin Mukyung couldn’t figure out when or how he was supposed to attack him.

Jin Mukyung licked his parched lips.

“I’ve never even met him… He praised me too highly.”

“No, honestly, you surprised me a little. I mean that.”

Jin Mukyung knew that everything Cheongpung was saying was sincere. That only made it feel stranger.

*Just a little?*

More than twenty years had passed since he began training with the sword. He had reached this point through talent and effort.

People had called him a genius, given him the martial title Heaven Shaking Sword, and counted him among the Ten Dragons and Phoenixes.

He had believed that he had never once been intoxicated by such hollow fame, but…

*I still have a long way to go.*

At some point, he must have grown accustomed to the gazes of people who looked up to him.

The wound Pung Yang had inflicted on him not long ago seemed to throb again.

“Do you know something?”

“What?”

“That you’re strong.”

“Until recently, I wasn’t certain. But now I know.”

“Because you met me?”

“Yes. Because I met Young Hero Jin. Now I know what the Ten Dragons and Phoenixes are capable of.”

“Is that so?”

Jin Mukyung let out a quiet laugh.

What an interesting guy. He possessed martial arts that rivaled—or even surpassed—those of an Elder of the Nine Sects and One Gang, yet he remained untainted by the world. He was pure. Honest.

He was a martial artist, but he didn’t fit in the Murim.

*He’s the exact opposite of someone I know.*

One person suddenly came to mind.

A guy who seemed like he could somehow survive no matter where he was thrown in the Murim, and who fought in the least martial-artist-like way imaginable.

“How old are you?”

“I’m twenty this year.”

“We’re the same age. Is it coincidence? Or fate?”

“What?”

Jin Mukyung shook his head instead of answering.

In truth, he already knew the outcome of this duel. The qi of the Zaha Divine Technique surging through Cheongpung’s entire body was that overwhelming.

It was merely regrettable that he couldn’t display all his abilities against an opponent of this caliber.

*How would that troublemaker handle a situation like this?*

Jin Mukyung glanced at his troublesome younger brother. With a grin like a little devil’s, Taekyung was mouthing something.

*You. Are. Fucked.*

*What a goddamn bastard.*

Laughing hollowly, Jin Mukyung placed a hand on his sword hilt. The internal energy boiling up from his dantian coursed through every part of his body.

Cheongpung looked at Jin Mukyung’s sword and spoke.

“My grandfather told me something else, too. A duel doesn’t need an opening stance or anything like that.”

“I agree.”

The next moment—

With a tremendous boom, violet light-flames and silver Sword Energy collided.
```
