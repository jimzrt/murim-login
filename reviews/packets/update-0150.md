<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0150.txt",
      "sha256": "37e624ec286e47fd141f4e7535ba8aebac5eae855345ad19817d89f158d27c90",
      "bytes": 15724
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "490efdfc5e1035e8f3542f31b4a03e477538db7c9c3848bb8dd5913dce11e45c",
      "bytes": 5458
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "429a7c226af420dc155675b1ee84180dec83b5641ea1e0fe4caeaab6ad996bba",
      "bytes": 33252
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "7733695f973e880b8a0073a74c4e686b10fdb5a7b68d8d2085b1c7ba4c91840e",
      "bytes": 1357
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "6e2c074cdeb62cd8a5f36d762c5043ec0397032c15ce23669dbd671178641787",
      "bytes": 1184
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "1c29902cc01bf7d2aefd29c9f027306ba03aa4f7af32de6bab58ed33e4fc09a6",
      "bytes": 5445
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "ec51c4084af581e6aae8248fd375c1d85a3fbcbb3c64d8680f3292a0dbba955e",
      "bytes": 1728
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "af38a84b1857ada5d934b5c1a812e299a786fd9abf6be24728b7a1fc107c04c2",
      "bytes": 613
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b193fb5db398d3a98898e3370f603fe2c0f30fa9b83d12220350670699923dbc",
      "bytes": 28865
    }
  ],
  "estimated_tokens": 27951
}
-->

# Durable State Update — Chapter 150

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 150. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 150. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 150,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 150,
    "continuity_sources": [150],
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
    "The City Lord’s luncheon attendance requirement has concluded; Prince Shangshan’s Token was obtained as the Quest Reward, and Zhu Bao is expected at the Jin Family’s grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, has no martial title yet, and began a duel with Jin Mukyung whose outcome is unknown.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader’s quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is a first-generation Huashan disciple known as Huashan’s Lone Crane and the first of the Three Plum Blossom Elites; he met Cheongpung ten years ago and is traveling with the other Elites to meet him again.",
    "Chulwoo and Eunhyang are Baek Museong’s junior disciples and fellow members of the Three Plum Blossom Elites; both are notorious troublemakers who caused trouble with the Black Serpent Sect while traveling.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung’s extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung’s side; they will remain at Honghwa Inn until New Year’s Day.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao’s autograph request three years earlier; Taekyung now promises to obtain Mukyung’s autograph for Zhu Bao at the upcoming banquet.",
    "The current Military Commissioner is incompetent, fond of bribes, and directly appointed and dismissed by the Emperor.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away, faces a large administrative workload, and prefers practical people with flexible thinking over rigid scholars; Hong Jin gave him one thousand silver nyang, prompting an extravagant pro-imperial welcome and a joking rapport between them."
  ],
  "continuity_sources": [
    149
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor’s reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is the outcome of Cheongpung’s duel with Jin Mukyung?"
  ],
  "safe_through": 149,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father’s cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”",
    "Render 서안 as “Xi’an,” 서악 as “Western Peak,” 흑사파 as “Black Serpent Sect,” 화산일학 as “Huashan’s Lone Crane,” 매화삼절 as “Three Plum Blossom Elites,” and 매화검수 as “Plum Blossom Swordsmen.”"
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

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 천무학관   | **Heaven's Gate Temple**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 임맥     | **Conception Vessel**                            |                                                       |
| 독맥     | **Governor Vessel**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 상태               | **Status**                     |
| 보상               | **Reward**                     |
| 청해     | **Qinghai**            |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 149
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 148
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; he formerly served the late Emperor, who ordered him to assist Prince Shangshan, and came to the frontier in something like exile; he remains the power behind the Shanxi Provincial Office, manages the City Lord's luncheon, and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft, candid about his fondness for bribes, and unwaveringly loyal to Prince Shangshan; he remains unashamed and matter-of-fact about having been castrated.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** The late Emperor ordered him to assist Prince Shangshan; Hong Jin has served the prince since infancy and remains loyal to him, while recognizing Taekyung as a young hero of the Jin Family of Taiyuan, increasingly enjoying his company and ruthless political methods, and forming an immediate joking rapport with Jin Wikyung.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 138
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 148
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered; recognized Cheongpung as Sword Saint Mae Jonghak's grandson and accepted his duel challenge despite his incomplete recovery
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 149
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search.

## Korean source

```text
＃150화



을씨년스러워 보일 정도로 넓고 휑한 연무장. 가부좌를 틀고 앉아 있는 한 청년의 이마에 땀방울이 흘러내렸다.

‘어찌했어야 했나.’

눈을 감고 생각에 잠긴다. 그리고 한 사람을 떠올린다.

그의 조잡한 청강검과 발걸음. 무공을 펼치기 시작하면서 사라진 웃음을 기억해 냈다.

비로소 칠흑 같은 어둠 속에서 자줏빛 광염을 두른 한 사람이 튀어나왔다.

‘청풍.’

검신 매종학의 손자, 제자. 뭐라 부르든 상관은 없다.

중요한 것은 나흘 전 그와 무공을 겨뤘고, 패했다는 사실이다.

진무경은 그날부터 연무장과 처소에 틀어박혀 두문불출했다. 허기는 벽곡단으로 채웠고 졸음은 수련으로 쫓았다.

지금 그에게 따뜻한 음식과 꿀 같은 휴식 따위는 필요하지 않았다.

‘졌다. 철저하게.’

불과 삼백여 초. 몸 상태가 정상이 아니었음을 감안해도 너무 쉽게 무너졌다.

자신이 누군가. 고작 약관에 절정의 경지에 올라 중원을 떠들썩하게 만들었던 천재다.

‘진천검, 십봉룡…… 우습군. 겨우 이 정도였나?’

고작 이 정도인 자신에게 붙은 거창한 별호들이 우습고, 허명이라 생각하면서도 은근히 스스로를 높게 여기던 자신의 모습이 허탈했다. 이거야말로 위선자 아닌가.

‘누가 그랬지. 천하는 넓다고.’

구주팔황(九州八荒), 사해오호(四海五湖).

이 광활한 대륙에 얼마나 많은 고수가 숨어 있단 말인가.

진무경은 청풍을 만나고서야 그 말의 진짜 의미를 깨달았다.

‘난 우물 안 개구리였어.’

천무학관(天武學館)은 분명 정파 무림 최고의 교육 기관이지만 천하의 모든 기재가 천무학관의 관도가 되는 것은 아니다.

천하 오대세가의 직계와 구파일방의 적전 제자들은 사문의 비전 절기를 이어받기에도 바쁘니까.

청풍도 그중 한 명이다. 그들은…… 우물 밖에서 태어났고 오래전부터 거기서 살아왔다.

‘기다려라, 청풍. 그리고 다른 놈들도 모두.’

눈이 반개한 순간, 진무경의 신형이 번개처럼 솟구침과 동시에 허리춤에서 빛이 뿜어져 나왔다.

쏴아아악!

검기(劍氣). 사방을 쉼 없이 난도질하는 은빛 검기는 나흘 전보다, 아니 지금까지의 그 어떤 때보다 짙고 선명했다.

청풍과의 비무는 그에게 깨달음과 투지를 주었다. 그저 강해지겠다는 막연했던 목표가 초점을 잡은 것이다.

쉬쉬쉬쉬슁!

그 후로도 진무경의 검은 쉬지 않았다. 지쳐 녹초가 되어 쓰러질 때까지…….



* * *



무림에서는 단전을 기해라고 부른다.

기해(氣海). 기의 바다. 몸 안의 모든 공력이 시작되고 모이는 곳. 누가 만들었는지 참 적절한 단어다.

띠링.



- [운기조식]을 시작합니다.

- [진가심법]의 구결을 따라 공력을 운용하십시오.



어느덧 팔 성에 오른 진가심법이다. 이미 수백, 수천 번도 넘게 반복했던 그 길을 따라 45년의 공력을 흘려보냈다.

‘뜨겁다.’

열화신단을 복용함으로써 얻은 열양지기(熱陽之氣)는 자그마치 반 갑자.

용암처럼 끓어오르는 강대한 기운이 전신의 혈맥을 휩쓸었다. 그 거침없는 기세를 보아하니 사뭇 기대감이 든다.

‘지금이라면 가능할지도…….’

운기조식을 할 때마다 항상 막히는 부분이 있었다. 철문처럼 굳게 잠긴 채 공력의 출입을 허락하지 않는 두 개의 혈도.

그곳을 임독양맥(任督兩脈)이라 부른다는 사실을 알게 된 건 최근의 일이다.

‘임독양맥. 소설에서 많이 봤지.’

무협 소설의 주인공이라면 한 번쯤 거치는 단계 아닌가?

무협 소설에선 임독양맥 뚫는 건 기본이요, 환골탈태는 옵션이다. 물론 난 주인공은커녕 조연도 안 되는 놈이라 번번이 물러나야 했다.

‘그랬었지. 지금까지는.’

고작 15년의 공력으로는 역부족이었다. 에어백도 안 터지는 소형차를 바위에 돌진시키는 꼴이니까.

하지만 이제는 다르다. 반 갑자의 열양지기가 더해진다면 소형차는 군용 전차로 탈바꿈한다.

‘이 정도면 해 볼 만하지.’

아니, 해내야 한다.

더 높은 경지로 나아가기 위해서는 반드시 넘어야 할 산이었다.

나는 기세가 최고조에 달한 공력을 끌어 올려 임맥과 독맥, 두 갈래로 쏘아 보냈다.

쿵!

혈도와 공력의 충돌음이 천둥처럼 들렸다. 동시에 찌르르한 고통이 척추와 아랫배를 울린다.

충돌하는 힘이 강해진 만큼 반발력도 장난이 아니다. 그러나 여기서 포기할 수는 없는 노릇. 나는 이를 악물고 연이어 부딪쳐 갔다.

쿵! 쿵! 쿵!

‘와, 씨. 뭐냐 이거.’

나도 나름대로 몸뚱이 험하게 굴린 놈이다. 칼 맞는 건 예사고 내장까지 망가진 적도 있다.

하지만 이건 고통의 종류가 다르다.

‘허리 아픈 건 그렇다 치고, 거기는 왜 아픈 건데!’

남자에게 목숨만큼이나 중요한 부위가 욱신거린다. 마치 누군가가 힘껏 움켜쥐었다가 놓기를 반복하는 것처럼.

임독양맥만 뚫으면 엄청난 보상을 받을 수 있을 것 같은데, 이것만 견디면 절정 고수가 될 수 있을 것 같은데…… 공력을 부딪쳐 갈수록 눈앞이 노래진다.

“으헉!”

삐빅!



- [운기조식]에 실패했습니다.

- 공력이 흐트러지며 혈도가 미세한 손상을 입었습니다.

- [근맥]이 1 하락합니다.



불알 아픈 것도 서러워 죽겠는데 근맥까지 떨어졌다. 나는 아직도 욱신거리는 그 부위를 붙잡고 침상 위에 엎드렸다.

“억! 어어억!”

벼는 익을수록 고개를 숙이고, 남자는 급소가 아플수록 허리를 숙이는 법.

기도드리는 심정으로 한참을 엎드려 있자 점차 통증이 사그라든다.

“훅, 후욱.”

하마터면 홍진 될 뻔.

땀범벅이 된 채로 침상에 드러누워 있는 그때, 다급한 발소리와 함께 불청객들이 들이닥쳤다.

“조장!”

“은인!”

문을 박차고 뛰어 들어온 혁무진과 청풍이 나를 보고 멈칫했다.

“무슨 일…… 헐.”

“은인, 뭐 하시는 거예요?”

“응? 뭐가?”

되묻고 나서 깨달았다.

내가 지금 어떤 꼴인지를.

“아.”

밀폐된 방. 한겨울임에도 어쩐지 땀으로 흠뻑 젖어 침상 위에 누운 채 손은 그곳을 붙잡고 있는 혈기왕성한 20대 청년.

음. 확실히 오해의 소지가 있군.

나는 침착하게 입을 열었다.

“오해야.”

잠깐의 침묵 끝에 혁무진이 눈웃음을 쳤다.

“압니다. 다 알아요.”

“아니라니까.”

“어허, 왜 이러십니까, 선수들끼리.”

“선수는 무슨 선수야, 이 미친놈아.”

“끝까지 모르는 척하시네. 제가 그리 속 좁은 놈으로 보이십니까?”

“아, 진짜 아니라고!”

“좋으셨어요? 어떻게, 아직 안 끝나셨으면 자리 비켜 드려요?”

“시작도 안 했어!”

“아, 그럼 이제 슬슬 시작하려고 하셨구나. 끝나면 다시 올까요?”

“안 해! 할 생각 없어!”

“괜찮습니다. 부끄러운 거 아니에요. 저도 상태 좋은 날에는 하루 다섯 번도 하는데요, 뭘.”

“그거 진짜냐…… 아니, 근데 이 새끼가.”

혼돈. 파괴. 망가.

시간이 지날수록 오해만 깊어져 가는 대화를 듣던 청풍이 고개를 갸우뚱했다.

“뭐가 오해예요? 뭘 알아요?”

“청 소협, 진짜 몰라요? 조장님이 저러고 계신 이유를?”

“몰라요. 소피가 마려우셔서 그런 건가?”

“허어, 어찌 이럴 수가. 딱 한 번만 알려 드릴 테니 마음에 새기십쇼. 이게 다 피와 살이 되는 거예요. 인생이 달라진다니까요.”

“네!”

“지금 조장님의 손이 어디에 있습니까? 대답해 보세요.”

“아랫도리요.”

“그렇죠. 그럼 아랫도리에는 뭐가 있을까요?”

“속곳이요.”

“속곳! 좋습니다. 거의 다 왔어요. 그럼 속곳에는 뭐가 있을까요?”

“어? 그런데 지금은 아랫도리에 없어요.”

“예?”

“은인의 손이 이쪽으로 오고 있어요.”

“헉.”

쫙! 털썩.

정확히 아래턱을 조준한 귀싸대기다. 편안한 표정으로 스르륵 무너지는 혁무진을 청풍이 받아 들었다.

“아직 다 못 들었는데.”

“……그거 들어서 뭐 하시게?”

“한 번 들으면 피와 살이 되고 인생이 달라진다고 하셨잖아요. 그럼 좋은 거 아니에요?”

“…….”

생각해 보니 아주 틀린 말은 아니네.

이미 기절한 성교육 선생님을 시무룩한 얼굴로 바라보던 청풍이 물었다.

“그런데 아랫도리 붙잡고 뭐 하고 계셨어요?”

“…….”

남들이 들으면 진짜 오해하겠다.



* * *



“……이렇게 된 겁니다.”

팩트로 꽉꽉 채운 설명이 끝나자 어느새 깨어난 혁무진이 불퉁한 표정으로 중얼거렸다.

“그럼 처음부터 그렇다고 말씀을 하시지.”

“후우, 너 진짜 오늘 죽도록 맞아 볼래?”

“아, 그건 사양하겠습니다. 지금도 골이 울려요.”

혁무진이 눈을 찡그리며 고개를 흔들었다.

“그런데 갑자기 임독양맥은 왜 건드리신 겁니까? 조장님이 절정 내가고수도 아니고, 그렇다고 위험을 감수할 만큼 간 큰 분도 아니시잖아요.”

“……그냥 한 번 건드려 봤다.”

“예?”

“됐어. 시끄러우니까 입이나 다물어라.”

나는 눈을 동그랗게 뜬 혁무진을 향해 손을 휘휘 저었다.

나흘 전 진무경과 청풍의 비무를 보고 지금보다 훨씬 강해지고 싶다는 생각이 들었다고 털어놓기에는 너무 낯부끄럽다.

“아무튼, 보기 좋게 실패했다는 것만 알아 둬. 거기가 아파서 제대로 못 하겠더라. 이거 왜 이러는 거야?”

“그거야 저도 모르죠. 의원도 아니고, 또 누구 같은 절정 고수도 아니니까.”

나와 혁무진의 시선이 자연스럽게 옆으로 옮겨 갔다. 앞서 말한 ‘누구 같은 절정 고수’가 눈을 깜빡이더니 입을 열었다.

“음, 할아버지한테 들은 적이 있어요.”

이제는 혁무진도 청풍의 신분을 안다. 우리는 동시에 기대감 어린 탄성을 토해 냈다.

“오오.”

“오오오.”

검성 매종학은 천하에서도 손에 꼽히는 고수. 무공에 관한 한, 그가 한 말이라면 팥으로 메주를 쑨다고 해도 믿을 수 있다.

“뭐라고 하셨는데요?”

“임맥은 자칫하다가는 사내구실 못 하게 되고, 독맥도 마찬가지라고. 그리고 또 뭐라고 하셨더라? 아, 맞다!”

곰곰이 생각에 잠겨 있던 청풍이 이마를 탁 쳤다.

“시간 지나면 알아서 뚫리니까 얌전히 놔두라고 하셨어요. 두 개 다 잘못 건드리면 병신 된다고.”

“……?”

“……?”

저게 뭔 소리야.

나와 혁무진의 시선이 거의 동시에 부딪쳤다.

“원래 임독양맥이 시간 지나면 뚫리는 거였냐?”

“글쎄요, 저도 처음 듣는 말인데.”

“그렇다고 허튼소리일 리는 없잖아. 검성씩이나 되는 양반인데.”

“그렇죠. 혹시 시간이 아주 많이 필요한 것 아닐까요?”

“얼마나 필요한데?”

“저야 모르죠. 저희 아버지가 내일모레 환갑이신데 한번 여쭤볼까요?”

“아, 임독양맥 뚫리셨냐고?”

“네.”

“무인이셔?”

“혁가 포목점 주인이신데요.”

“너는 될 수 있으면 말하지 마라. 듣는 사람 속 터지니까.”

“네.”

이런 놈을 수하라고 데리고 다니는 내가 불쌍하다.

나는 한숨을 푹 내쉬고 청풍에게 말했다.

“좀 더 자세히 설명해 주실 수 있나요? 설마 조부님께서 그것만 딱 말씀하시진 않았을…….”

“딱 그것만 말씀하셨어요.”

“……진짜요? 토씨 한 글자 안 틀리고?”

“저는 은인께 거짓말을 하지 않아요.”

하긴, 청풍은 거짓말 칠 정도로 약은 놈이 아니다.

천성인지, 아니면 성장 환경 때문인지 나쁘게 말하면 멍청해 보일 정도로 솔직하고 해맑다.

청풍이 억울한 표정으로 덧붙였다.

“그리고 저희 할아버지도 거짓말을 하시는 분이 아니세요. 저도 기다리니까 뚫렸는걸요. 임독양맥 전부는 아니고 독맥 하나뿐이지만.”

“검성 어르신께서 거짓말을 하셨다는 게 아니라…… 잠깐만요, 지금 뭐라고요?”

“청 소협. 방금 뭐라 하셨습니까? 임독양맥을 뚫으셨다고요?”

“어, 일단은 독맥 하나만요. 아직 제가 어려서 그런가 봐요.”

나는 더듬더듬 물었다.

“어, 어떻게 뚫으셨는데요?”

“재작년에 그냥 수련하다가 기분이 묘해지고, 꽝!”

“꽝?”

“그렇게 뚫었어요.”

“…….”

“…….”

“신기해서 할아버지께 여쭤봤더니 그게 깨달음이란 거래요. 헤헤.”

안 되겠다. 달라도 너무 달라.

시간이 흐르면 자연히 임독양맥을 타통 할 거라는 검성의 말은 정확했다.

문제는 오직 청풍에게만 적용된다는 것이다.

눈앞에서 해맑게 웃고 있는 이놈은, 애초에 나 같은 놈과는 종(種)이 다른 신인류나 다름없다.

‘천재. 하늘이 내린 재능이다, 이거지.’

청풍도, 진무경도. 애시당초 나와는 타고난 재능이 다르니 답이 없다.

말문이 막혀 한동안 가만히 있자 청풍이 슬금슬금 내 눈치를 살폈다.

“은인, 제가 뭐 잘못한 거예요?”

“아뇨. 잘못한 거 없어요.”

“그래요? 다행이다.”

안도의 한숨을 쉬는 청풍을 보며 바짝 마른 입술을 핥았다.

“그런데 저기…….”

“네?”

“부탁 하나만 해도 될까요?”

“뭐든지 말씀하세요.”

젠장, 이거 막상 말하려니 입이 잘 안 떨어지네.

나는 철판이 두껍다. 뻔뻔하다는 소리도 들어 봤고, 염치없다는 소리도 들어 봤다.

하지만 이 한마디가 왜 이렇게 힘들까.

“은인?”

나는 어렵게, 정말 어렵게 한마디를 내뱉었다.

“제 수련 좀 도와주실 수 있나요?”

“그럼요. 물론이죠.”

“네?”

“도와드릴게요. 수련.”

녀석의 투명한 눈동자를 바라본 순간, 비로소 깨달았다. 내가 왜 망설였는지.

그건 호승심이었다.

이 녀석에게만큼은 도움을 받고 싶지 않다는 호승심.

싫어서가 아니라 오롯이 내 힘으로 꺾고 싶은 상대라서 생기는 감정이었다.

“……너무 쉽게 승낙하시는 것 아니에요?”

“은인한테는 빚을 많이 졌는걸요. 제가 좋은 거 여러 가지 많이 가르쳐 드릴게요. 아, 물론 할아버지한테 주의받은 무공은 빼고!”

가르쳐 준다고?

내 좁쌀 같은 마음 한구석이 불편해진다. 그리고 확실해졌다.

나는 이 녀석을 꺾고 싶다. 동등한 위치에 서고 싶다.

하지만 그러기 위해선…….

“그럼 잘 부탁드릴게요.”

배워야지, 뭐.

나, 생각보다 낯짝 두꺼운 놈이다.
```

## Final English reading copy

```markdown
# Chapter 150

The training ground was so wide and empty that it looked bleak. Sweat trickled down the forehead of a young man sitting cross-legged.

*What should I have done?*

He closed his eyes and sank into thought. Then he recalled one person.

He remembered Cheongpung’s crude blue-steel sword and clumsy footwork. He remembered the smile that vanished when the young man began to display his martial arts.

At last, from the pitch-black darkness, a figure wrapped in violet light-flames burst forth.

*Cheongpung.*

Grandson and disciple of the Sword God Mae Jonghak. It made no difference what he called him.

What mattered was the fact that four days ago, he had exchanged martial arts with Cheongpung—and lost.

Jin Mukyung had shut himself away in the training ground and his quarters ever since that day. He staved off hunger with fasting pills and chased away sleep through training.

Warm food and honey-sweet rest were of no use to him now.

*I lost. Completely.*

It had taken barely three hundred exchanges. Even taking into account the fact that his condition had not been normal, he had fallen far too easily.

*Who am I?* He was a genius who had reached the Peak realm at barely twenty and caused the Central Plains to tremble.

*Heaven Shaking Sword. Ten Dragons and Phoenixes… How laughable. Was that all I amounted to?*

The grand titles attached to someone as mediocre as himself seemed laughable, nothing more than empty reputations. And yet the way he had secretly held himself in high regard left him feeling hollow.

*Isn’t that the very definition of hypocrisy?*

*Who was it that said the world was vast?*

The Nine Provinces and Eight Wastes. The Four Seas and Five Lakes.

How many masters were hidden across this enormous continent?

Only after meeting Cheongpung did Jin Mukyung understand the true meaning of those words.

*I was a frog in a well.*

Heaven’s Gate Temple was certainly the greatest educational institution in the orthodox Murim, but not every genius under heaven became a student at Heaven’s Gate Temple.

The direct descendants of the Five Great Families and the direct disciples of the Nine Sects and One Gang were too busy inheriting their sects’ secret ultimate techniques.

Cheongpung was one of them. They had been born outside the well and had lived there for a long time.

*Wait for me, Cheongpung. And all the others, too.*

The moment his eyes opened halfway, Jin Mukyung’s body shot upward like lightning, and light burst from his waist.

Whoosh!

Sword Energy. The silver Sword Energy slashed incessantly in every direction. It was denser and clearer than it had been four days ago—no, than it had ever been before.

His duel with Cheongpung had given him insight and fighting spirit. His vague goal of simply becoming stronger had finally gained focus.

Swish, swish, swish, swish!

Jin Mukyung’s sword did not stop after that, either.

Not until he was exhausted, utterly spent, and collapsed…

* * *

In Murim, the dantian is called the qi sea.

The qi sea. The sea of qi. The place where all the internal energy in the body begins and gathers. Whoever coined the term had chosen very well.

Ding!

> **System**
>
> Qi circulation has begun.
>
> Follow the formula of the Jin Family’s Cultivation Technique to circulate your internal energy.

The Jin Family’s Cultivation Technique had reached the eighth stage. Following the path I had already repeated hundreds, even thousands, of times, I sent forty-five years of internal energy flowing through it.

*Hot.*

The Scorching Yang Qi I had gained by taking the Blazing Flame Divine Pill amounted to half a jiazi.

The powerful energy boiling like lava swept through every blood vessel in my body. Seeing its unstoppable momentum, I began to feel a little hopeful.

*Maybe it’s possible now…*

There was always one part that blocked me whenever I circulated my qi. Two acupoints locked as firmly as iron gates, refusing to let internal energy pass through.

I had only recently learned that they were called the Conception and Governor Vessels.

*The Conception and Governor Vessels. I’ve seen them a lot in novels.*

Wasn’t this a stage every protagonist in a martial arts novel passed through at least once?

In martial arts novels, opening the Conception and Governor Vessels was the bare minimum, while Bone Transformation was optional. Of course, I was neither a protagonist nor even a supporting character, so I had been forced to retreat every time.

*That was then. Until now.*

Fifteen years of internal energy had been insufficient. It was like driving a compact car whose airbags did not even work straight into a boulder.

But things were different now. If half a jiazi of Scorching Yang Qi were added to the mix, the compact car would be transformed into a military tank.

*This should be worth a try.*

No. I had to do it.

It was a mountain I absolutely had to cross if I wanted to advance to a higher realm.

I drew up the internal energy that had reached its peak and shot it down two paths, toward the Conception Vessel and the Governor Vessel.

Boom!

The collision between my internal energy and the acupoints sounded like thunder. At the same time, a sharp pain rang through my spine and lower abdomen.

The stronger the collision became, the more vicious the recoil was. But I could not give up here. I clenched my teeth and kept crashing into them.

Boom! Boom! Boom!

*What the hell is this?*

I had put my body through hell in my own way. Being stabbed was nothing unusual, and I had even suffered damage to my internal organs before.

But this was a completely different kind of pain.

*I can accept my lower back hurting, but why does it hurt there?*

A part of a man as important as his life throbbed painfully. It felt as though someone were squeezing it as hard as they could, releasing it, and then repeating the process.

It felt as though I would receive an incredible reward if I opened the Conception and Governor Vessels. It felt as though I would become a Peak master if I could only endure this…

But the more I slammed my internal energy against them, the more the world before my eyes turned yellow.

“Ugh!”

Beep! Beep!

> **System**
>
> Qi circulation failed.
>
> Your internal energy became disordered, causing slight damage to your acupoints.
>
> **Sinews and Meridians** decreased by 1.

My balls were already aching badly enough to make me miserable, and now my Meridians had dropped, too.

I grabbed the still-throbbing area and collapsed face-first onto the bed.

“Ugh! Uuugh!”

As rice bows its head more deeply the riper it becomes, a man bows at the waist more deeply the more his vital points hurt.

I stayed hunched over for a long while as though praying, and the pain gradually subsided.

“Huff, huff.”

I had almost ended up like Hong Jin.

Just as I sprawled out on the bed, drenched in sweat, hurried footsteps approached, and unwelcome guests burst in.

“Captain!”

“Benefactor!”

Hyuk Mujin and Cheongpung rushed through the door, then stopped short when they saw me.

“What happened… Whoa.”

“Benefactor, what are you doing?”

“Huh? What about it?”

I asked the question, then realized it.

I realized what I looked like right now.

“Oh.”

A twenty-something young man in a sealed room, soaked in sweat despite the middle of winter, lying on a bed with one hand clutching that particular spot.

Hmm. There was definitely room for misunderstanding.

I calmly opened my mouth.

“You’ve got it wrong.”

After a brief silence, Hyuk Mujin smiled with his eyes.

“I know. I know everything.”

“No, you don’t.”

“Oh, come on. Why are you acting like this? We’re both professionals.”

“What do you mean, professionals, you lunatic?”

“You’re still pretending not to know. Do I look like such a narrow-minded man to you?”

“I’m telling you, that’s not what it is!”

“Did you enjoy yourself? If you haven’t finished yet, should I step outside?”

“I haven’t even started!”

“Oh, then you were just about to start. Should I come back when you’re done?”

“I’m not doing it! I have no intention of doing it!”

“It’s all right. There’s nothing to be embarrassed about. I do it five times a day when I’m in good shape.”

“Is that actually true…? No, wait. You little—”

Chaos. Destruction. A complete mess.

As the conversation only grew more suspicious with every passing moment, Cheongpung tilted his head.

“What’s the misunderstanding? What does he know?”

“Young Hero Cheongpung, you really don’t know why the Captain is like that?”

“I don’t. Does he need to pee?”

“What? How can this be? I’ll only explain it once, so remember this well. All of this becomes flesh and blood. I’m telling you, it changes your life.”

“Yes!”

“Where is the Captain’s hand right now? Answer me.”

“On his lower half.”

“That’s right. And what’s on the lower half?”

“Underclothes.”

“Underclothes! Good. You’re almost there. And what’s inside the underclothes?”

“Huh? But right now it isn’t on his lower half.”

“What?”

“Benefactor’s hand is coming this way.”

“Gasp.”

Smack!

Thud.

It was a slap aimed precisely at his lower jaw. Hyuk Mujin crumpled with a peaceful expression, and Cheongpung caught him.

“I haven’t heard the whole thing yet.”

“…What are you going to do with the rest of it?”

“You said that hearing it would make it flesh and blood and change my life. Isn’t that a good thing?”

“…”

Come to think of it, that wasn’t entirely wrong.

Cheongpung looked dejectedly at the sex-education teacher who had already passed out.

“But what were you doing while holding your lower half?”

“…”

If anyone else heard this, they would definitely misunderstand.

* * *

“…And that’s what happened.”

By the time I finished an explanation packed full of facts, Hyuk Mujin had woken up and was muttering with a sullen expression.

“Then you should have said that from the beginning.”

“Whew. Do you really want me to beat you to death today?”

“Ah, I’ll pass. My head is still ringing.”

Hyuk Mujin winced and shook his head.

“But why did you suddenly try to open the Conception and Governor Vessels? You’re not a Peak internal-energy master, and you don’t have the guts to risk something like that.”

“…I just tried it once.”

“What?”

“Forget it. You’re noisy, so shut your mouth.”

I waved my hand at Hyuk Mujin, who had opened his eyes wide.

It was too embarrassing to admit that seeing the duel between Jin Mukyung and Cheongpung four days ago had made me want to become much stronger than I was now.

“Anyway, just know that I failed spectacularly. I couldn’t do it properly because it hurt there. Why is this happening?”

“I wouldn’t know. I’m not a physician, and I’m not some Peak master either.”

Hyuk Mujin and I naturally turned our gazes to the side. The aforementioned “Peak master” blinked and opened his mouth.

“Hmm. I’ve heard something about it from my grandfather.”

Hyuk Mujin knew Cheongpung’s identity now, too. We both let out exclamations full of anticipation.

“Ohhh.”

“Ooooooh.”

The Sword Saint Mae Jonghak was one of the most highly regarded masters under heaven. When it came to martial arts, if he had said it, we could believe him even if he told us that red beans could be made into soybean blocks.

“What did he say?”

“He said that if you mess up the Conception Vessel, you might not be able to perform as a man, and that the same goes for the Governor Vessel. And what else did he say? Oh, right!”

Cheongpung, who had been thinking hard, smacked his forehead.

“He said they would open on their own with time, so I should leave them alone. He said touching either of them incorrectly would turn me into a cripple.”

“…”

“…”

*What the hell is he talking about?*

Hyuk Mujin and I exchanged glances almost simultaneously.

“Do the Conception and Governor Vessels normally open with time?”

“I don’t know. That’s the first I’ve heard of it, too.”

“But it couldn’t be nonsense. He’s the Sword Saint, after all.”

“Right. Perhaps it takes a very long time?”

“How long?”

“How would I know? My father is almost sixty. Should I ask him?”

“Oh, ask him whether his Conception and Governor Vessels have opened?”

“Yes.”

“Is he a martial artist?”

“He owns the Hyuk Family Textile Shop.”

“Try not to talk if you can help it. You’ll drive the listener insane.”

“Yes.”

I pitied myself for taking someone like this around as my subordinate.

I let out a deep sigh and spoke to Cheongpung.

“Could you explain in a little more detail? Surely your grandfather didn’t say only that…”

“He said exactly that.”

“…Really? Word for word?”

“I don’t lie to my Benefactor.”

That was true. Cheongpung was not clever enough to lie.

Whether it was in his nature or the result of his upbringing, he was so honest and guileless that, put unkindly, he looked stupid.

Cheongpung added with an indignant expression,

“And my grandfather isn’t someone who lies, either. I waited, too, and mine opened. Not both of them—just the Governor Vessel.”

“The Sword Saint didn’t lie… Wait. What did you just say?”

“Young Hero Cheongpung, what did you say? You opened the Conception and Governor Vessels?”

“Oh, only the Governor Vessel for now. Maybe it’s because I’m still young.”

I asked haltingly,

“How did you open it?”

“Two years ago, I was training when I suddenly felt strange, and then—bang!”

“Bang?”

“That’s how it opened.”

“…”

“…”

“I thought it was strange, so I asked my grandfather about it. He said it was enlightenment. Hehe.”

This was hopeless. We were far too different.

The Sword Saint had been right that the Conception and Governor Vessels would open naturally with time.

The problem was that it only applied to Cheongpung.

The young man smiling brightly in front of me was practically a new species of humanity, fundamentally different from someone like me.

*Genius. Talent bestowed by heaven. That’s what this is.*

Cheongpung and Jin Mukyung. Their innate talent was different from mine from the very beginning. There was no answer for me.

When I remained silent for a while, Cheongpung cautiously watched my expression.

“Benefactor, did I do something wrong?”

“No. You didn’t do anything wrong.”

“Really? That’s a relief.”

As Cheongpung sighed in relief, I licked my dry lips.

“But, um…”

“Yes?”

“Can I ask you for a favor?”

“Tell me whatever it is.”

Damn it. Why was it so hard to say now that the moment had come?

I had thick skin. I had been called shameless, and I had been called without shame.

But why was this one sentence so difficult?

“Benefactor?”

With great difficulty—truly, great difficulty—I forced out the words.

“Could you help me with my training?”

“Of course. Certainly.”

“What?”

“I’ll help you. With your training.”

As I looked into his clear eyes, I finally understood why I had hesitated.

It was competitive pride.

The competitive pride that made me unwilling to accept help from this young man of all people.

It was not because I disliked him. It was because he was an opponent I wanted to bring down solely through my own strength.

I wanted to stand on equal footing with him.

But to do that…

“Then I’ll be counting on you.”

I had to learn. What else could I do?

Turns out I had a thicker hide than I thought.
```
