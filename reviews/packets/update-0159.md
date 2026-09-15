<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0159.txt",
      "sha256": "e0de28129aa16fcfa5c894a2de918c19a1f4afff48044545efe740c4955e70f1",
      "bytes": 18012
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "170c057e4b54d7a3f2dcfb9ceca326ac8899eef9a42f579cf2bd84ef8d89fb04",
      "bytes": 6972
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0bf73ec67ba1435076d234b9b2371b38a2eaa5657033251178f60d279a4d4d72",
      "bytes": 38062
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a880d1313b63c8dcf956609823d343bc726abab6894232772a643aa8a8a4431c",
      "bytes": 1661
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fcf30dded8f63495c8a318abc3a235db150638949a3fb3286e3d8be4b2d547a1",
      "bytes": 5558
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "112bb4b3850b8a94e9e42cc5ea03dd7c6576aa31816a74b1d83828baa8adf21d",
      "bytes": 1826
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "68faeaa95e5fad81d4ae7aa44552cfc66fc36840f43b909e98019a499f8a94b2",
      "bytes": 613
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c2066d005a93169fbb58c4fd589436a684e7efe69f7af5263349ffc1b87526e9",
      "bytes": 30130
    }
  ],
  "estimated_tokens": 31019
}
-->

# Durable State Update — Chapter 159

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 159. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 159. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 159,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 159,
    "continuity_sources": [159],
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
    "The City Lord's luncheon requirement concluded with Prince Shangshan's Token obtained as the Quest Reward; Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy, though his internal energy and physique are now showing signs associated with preparation for that realm.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is twenty years old, a Peak master raised by Mae Jonghak, knows numerous Huashan martial arts, can use the Zaha Divine Technique and Sword Energy, has no martial title, and teaches Taekyung and Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence for at least ten years; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is Huashan's Lone Crane and the first of the Three Plum Blossom Elites; Chulwoo and Eunhyang are his junior disciples and fellow Elites, and all three are traveling to meet Cheongpung again.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk; the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served him since infancy, and is the power behind the Shanxi Provincial Office.",
    "Jin Mukyung lost to Cheongpung four days before the luncheon, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Jin Wikyung is the thirty-five-year-old Lesser Family Head and future Family Head, directing the Jin Family's expansion and branch stabilization while aiming to establish it as a great family.",
    "Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Taekyung has a private training ground in a rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung.",
    "Wall Lizard Technique training is complete: Taekyung and Mujin climbed the cliff ten times, Taekyung acquired the technique, gained 10 Stat Points and 10 Skill Points, and upgraded Beginner Trainee to Intermediate Trainee.",
    "Wipeng offered to personally lead useful martial artists against approximately five hundred mounted bandits gathering near Datong; Huashan sent the Three Plum Blossom Elites and reported Mae Jonghak missing.",
    "Taekyung's second Cheongpung-training Quest requires him to defeat Cheongpung at least once before New Year's Day.",
    "Cheongpung had only ever sparred with Mae Jonghak before leaving Huashan and is adjusting with difficulty to fighting people outside his grandfather's instruction; he considers Taekyung and Jin Mukyung the strongest people he has met since leaving Huashan.",
    "Cheongpung identifies Taekyung's rough, unrefined martial arts and naturally emerging aura as Wildness; Taekyung can increasingly read and imitate Cheongpung's forms during sparring.",
    "Hyuk Mujin has resolved to become strong enough to be remembered as Jin Taekyung's right arm or heart and by the name Hyuk Mujin; he is now Level 50 after recent training and sparring."
  ],
  "continuity_sources": [
    158
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him, and did he actually go to the Jin Family after breaking seclusion to find Cheongpung?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?",
    "Can Taekyung defeat Cheongpung before New Year's Day?"
  ],
  "safe_through": 158,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally; render 초일류 as “advanced First Rate,” 군문 as “military,” 풍운검군 as “Wind-and-Cloud Sword Lord,” and 오촌 당숙 as “father's cousin.”",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” 광염 as “light-flames,” 검명 as “Sword Cry,” and 창명 as “Spear Cry.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” and 환골탈태 as “Bone Transformation.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 태초 마을 as “Taecho Village,” 벽호공 as “Wall Lizard Technique,” and 낙안봉 as “Falling Goose Peak.”",
    "Render 황하방 as “Yellow River Gang,” 소공문 as “Sogong Sect,” 남부상회 as “Southern Merchant Guild,” 내당주 as “Inner Hall Master,” 내외당 as “Inner and Outer Halls,” and 세가 as “great family.”",
    "Render 암향표 as “Dark Fragrance Drift,” 복호권 as “Crouching Tiger Fist,” 천근추 as “Thousand-Catty Drop,” 야성 as “Wildness,” 오행매화보 as “Five-Element Plum Blossom Steps,” and 공수납백인 as “Empty-Hand Seizes the Blade.”",
    "Retain Taekyung's instant-noodle flavor joke with “mild Neoguri,” “Jin Ramen spicy flavor,” and “Puramyeon spicy flavor”; render 천근거력 as “the force to move a thousand catties.”"
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
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 태초 마을 | **Taecho Village** | Place named by Taekyung immediately after surviving the fall. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 검성 수련 간접 체험기 | **Sword Saint Training: A Secondhand Experience** | Cheongpung's Peak-grade cliff-training Quest. |
| 검성 수련 간접 체험기-2 | **Sword Saint Training: A Secondhand Experience—2** | Linked Quest generated after the first training Quest succeeds. |
| 초보 수련자 | **Beginner Trainee** | System Title upgraded after the tenth cliff climb. |
| 중급 수련자 | **Intermediate Trainee** | System Title received after Beginner Trainee is upgraded. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 태극 1장부터 8장까지 | **Taegeuk Forms 1 through 8** | Standard taekwondo pattern sequence Taekyung copied as a child. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |

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
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 초식     | **form**                                         | Numbered technique movement                           |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 진가보법   | **Jin Family's Manoeuvre Technique**   |
| 진가창법   | **Jin Family's Spear Technique**       |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 158
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 158
- **Aliases:** None revealed
- **Role:** Level 50 First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, persistent, and possessed of clear martial talent; suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 158
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered; four days before this chapter, he lost his duel with Cheongpung after roughly three hundred exchanges, secluded himself to train, and sharpened his Sword Energy while resolving to surpass Cheongpung and the other geniuses
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 158
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search.

## Korean source

```text
＃159화



민첩에 50포인트. 그리고 근력에 50포인트.

합치면 자그마치 100포인트. 열 번의 레벨 업을 거쳐야 얻을 수 있는 막대한 포인트를 한 번에 쏟아부었지만 하나도 아깝지 않다.

‘역시 포인트가 최고야. 늘 짜릿해. 새로워.’

지면을 박차는 발끝이, 창대를 움켜쥔 손아귀가 외친다.

지금의 나는 불과 몇 초 전보다 훨씬 강하다고.

그리고 이제야 이 비무에서 승리할 수 있는 첫걸음을 내디뎠다고.

‘속전속결로 끝낸다.’

후우우웅!

무시무시한 파공성과 함께 창날이 내리꽂히는 순간, 청풍의 전신에서 자줏빛 아지랑이가 피어올랐다.

‘자하신공(紫霞神功).’

드디어 청풍이 전력을 다하기 시작했다는 증거다. 하지만 이번 승부에 있어 가장 중요한 것이 하나 남아 있었다.

쉬이이익!

아니나 다를까, 한 줄기 검기가 청풍의 허리춤에서 솟구쳤다.

절정 고수의 전유물인 검기는 강철도 베어 버리는 절삭력을 지녔다.

아직 절정의 벽을 넘어서지 못한 나로서는 받아칠 수 없다.

한발 물러서거나, 창이 파괴되는 걸 계산에 넣고 다음 공격을 이어 가야 한다.

그런데…….

‘이 기분은 뭐지?’

묘한 기시감. 심장이 쿵쿵 뛰고 시야가 선명해진다. 느려진 세상 속, 손아귀에 잡힌 서늘한 창대가 부르르 진동했다.

우웅, 우우웅.

머리는 차갑게. 가슴은 뜨겁게.

7년간 그렇게 싸워 왔는데…… 이번에는 다르다. 그야말로 본능. 오직 본능만이 내 모든 것을 지배했다.

‘할 수 있다.’

나는 홀린 사람처럼 내리치는 창날에 힘을 더했다.

45년의 공력이 손끝을 타고 창날을 향해 내달렸다. 손아귀의 진동이 한층 커졌고, 자줏빛 검기가 눈부셨다.

그뿐이었다.

쾅!

거대한 두 힘의 충돌. 무지막지한 굉음과 풍압(風壓), 커다랗게 뜨인 청풍의 두 눈. 그리고…….

‘멀쩡해.’

새하얀 창날이 있다.

청풍의 검기를 짓누르고 있는 창날은 실금 하나 가지 않은 모습으로 진동했다.

우우우웅. 마치 수백 마리의 벌들이 날갯짓하는 듯하다.

‘도대체 어떻게?’

이것도 근력 상승의 효과인가? 아니면 단순한 우연?

그 순간, 의문에 대한 답이 들려왔다.

띠링.



- 당신은 새로운 경지에 발을 디딜 준비를 끝마쳤습니다.

- 병장기가 당신의 기운에 공명합니다.

- 퀘스트, [벽을 넘어서]가 생성되었습니다.



‘아.’

근력 상승의 효과도, 단순한 우연도 아니었다.

이건 순리다. 나는 수많은 인고 끝에 마침내 벽을 마주했고 이젠 그 벽을 넘어서야 한다.

무수한 이들이 넘어서지 못한 절정이라는 벽을.

‘절정 고수.’

검기(劍氣), 혹은 오러(Aura)를 다루는 진정한 초인들.

생각만으로도 전율이 흐른다. 지난 기억들이 싸구려 모노 필름처럼 펼쳐져 눈앞을 스쳤다.

널리고 널린 일개 F급 헌터가 여기까지 왔다. 수많은 위기가 있었고 누군가의 희생이 있었다.



퀘스트, [벽을 넘어서]를 수락하시겠습니까?

Y   /   N



수도 없이 생사를 넘나들었던 나다. 절정의 벽 정도는 가뿐히 넘어 줘야 내가 살아온 나날들에 부끄럽지 않을 것이다.

‘당연히 예스지.’



- 퀘스트를 수락하셨습니다!



띠링. 경쾌한 시스템 알림과 동시에 나는 입꼬리를 끌어 올렸다.

생각은 길었지만 지나간 시간은 짧았다. 당황한 눈빛으로 나를 올려다보고 있는 청풍에게 속삭였다.

“자, 지금부터는 푸라면 매운맛.”

한국인의 매운맛을 보여 주마.



* * *



꾸구구국.

약 1분 전과 비교하면 25퍼센트나 상승한 근력이다. 그야말로 하늘과 땅 차이. 내 갑작스러운 변화에 청풍은 당황스러운 기색이 역력했다.

“으, 은인. 갑자기 이런 힘이 어디서.”

“한국인 밥심이지. 그중에서도 특히 국밥.”

“예?”

“아침마다 뼈 해장국을 두 그릇씩 먹었거든. 공깃밥은 다섯 공기.”

“그게 무슨…… 헉!”

꾸구구국.

점점 더 더해 가는 힘에 청풍이 헛숨을 삼켰다. 녀석에게는 검기와 자하신공이 있었지만 큰 효력을 발휘하지 못했다.

내 기운을 한껏 머금은 채 공명하는 창은 이제 검기로도 가를 수 없을 만큼 강건했으니까.

‘충분히 승산이 있다.’

그러나 청풍은 그리 호락호락한 놈이 아니었다.

“합!”

짧은 기합성과 함께 어마어마한 힘이 창날을 위로 튕겨 냈다.

고작해야 한 뼘 떨어졌을 뿐이지만 순간적으로 압박을 벗어난 청풍은 기회를 놓치지 않았다.

“미안해요. 제가 은인을 너무 쉽게 봤어요.”

말이 끝나기도 전에 녀석의 손바닥에서 무형의 기운이 쏘아졌다.

태을미리장(太乙迷離掌). 검성이 몸소 가르쳐 주었다는 화산파의 비전 절기다.

“흡!”

퍼버벅! 찌릿한 고통과 함께 연거푸 다섯 걸음을 물러났다.

레벨 업 하는 족족 근골과 근맥을 올려놔서 망정이지, 아니었다면 큰 낭패를 볼 뻔했다.

“젠장, 아픈데?”

그런 나를 청풍이 놀란 토끼 눈으로 바라봤다.

“칠성의 태을미리장을…….”

“그런 말 하지 마십쇼. 괜히 사이다 먹고 싶어지잖아.”

“예?”

그래, 저 반응 나올 줄 알았지.

청풍이 되묻는 순간, 내 창은 이미 녀석의 가슴을 찌르고 있었다.

완벽한 타이밍의 기습. 하지만 겨우 이 정도로 끝날 리 없다. 내 생각에 그렇다고 대답이라도 하듯 검기가 창날을 후려쳤다.

카캉!

‘기대도 안 했다.’

기대가 없으니 실망도 없다. 감정이 흔들리지 않았으니 초식도 마찬가지였다.

‘다음은 허리.’

쐐애액!

창이 움직임과 동시에 청풍이 허리를 틀었다. 창날이 일으킨 풍압이 녀석의 상의를 소리 없이 베었다. 드러난 살에서 옅은 핏줄기가 비쳤다.

약간의 소득이라면 소득이다.

‘다음은 목.’

그대로 돌아서며 창대로 청풍의 목선을 후려쳤다.

쾅!

인간의 몸과 강철 창이 부딪쳤을 때 날 만한 소리가 아니다.

그러나 청풍에게는 무공이 있었다. 자하신공이라는, 천하에서 손꼽히는 내공심법이자 호신기공이.

나는 한층 짙어진 자줏빛 기운을 보며 혀를 내둘렀다.

‘아무리 그래도 그렇지, 어떻게 타격이 하나도 없을 수 있냐? 이건 완전 사긴데.’

매화 수저 보소. 이거 더러워서 비무 하겠나.

하지만 혀만 차고 있을 때가 아니었다. 고작 반보 만에 내 코앞까지 들이닥친 청풍이 흩뿌린 검기가 눈앞을 가득 메우고 있었다.

쉬이이익!

검 끝이 꽃송이를 피워 낸다. 유려하다 못해 아름다운 움직임. 그러나 넋 놓고 있다가는 북망산 안내판 앞에 서 있는 자신을 발견하게 될 거다.

지금껏 지켜본 매화검법은 무서운 무공이다. 매우 정교하고 복잡한 초식.

그런 무공이 청풍의 손에서 펼쳐지니 마치 빗속에 갇힌 느낌이었다.

하지만…….

‘볼 수 있다.’

눈을 부릅떴다. 호흡이 느려지고 시야가 선명해진다. 심장 뛰는 소리가 천둥처럼 들리고, 창이 부르르 떨렸다.

웅웅웅. 창이 울고 있다. 지금 이 순간, 나와 창은 한 몸이나 다름없다.

더 이상 창대가 서늘하게 느껴지지 않았다.

쉬쉬쉬쉬쉭!

검과 창이 뒤섞였다. 나는 빗발치는 검기를 쉼 없이 튕겨 내고 쳐 냈다.

열 번, 스무 번, 혹은 서른 번…….

청풍은 누구보다 집요하고 날카로웠다. 허리춤을 파고드는 검기를 받아치자 태을미리장이 날아왔고, 태을미리장을 피하자 복호권이 가슴을 노렸다.

퍽!

복호권을 막아 낸 어깨가 욱신거렸다.

찰나의 고통. 순간 움직임이 둔해진 나를 향해 청풍이 말아 쥔 주먹을 활짝 폈다.

나를 향한 다섯 개의 손가락 끝에서 공기가 터져 나갔다.

‘아, 빌어먹을. 저게 있었지.’

깨달음과 동시에 허리를 활처럼 뒤로 굽혔다.

진무경과의 비무에서 단 한 번 보여 준 매화오품지(梅花五品指)다.

피피핏! 다섯 줄기의 지력(指力)이 콧날과 귓불을 아슬아슬하게 스쳤다.

‘역시 강해.’

다시 한번 느꼈다. 청풍은 평범한 검수가 아니라는 사실을.

녀석은 검성 매종학의 후인일 뿐만 아니라 화산파의 절기를 섭렵한, 말하자면 화산파 무공 종합 선물 세트다.

나는 배어 나오는 피를 닦으며 슬쩍 입을 열었다.

“너무 세게 나오시는데?”

“그건 제가 은인께 드리고 싶은 말씀인데요? 솔직히 놀랐어요.”

“왜, 별 볼 일 없을 것 같던 놈이 예상보다 훨씬 잘 싸워서?”

“네!”

“…….”

“생각 이상이에요. 진심으로. 그리고…….”

“그리고?”

“재밌네요.”

청풍의 입가에 희미한 웃음을 보며 생각했다.

호승심을 떠나 이 녀석은 무공, 그 자체를 좋아한다. 즐기는 천재란 이렇게 무서운 존재라는 것을 내게 입증하고 있다.

“은인도 저랑 같지 않나요?”

“청 소협, 내 꿈이 뭔지 알아?”

“……?”

“몸 성히 은퇴해서 내 명의로 된 빌딩 하나 세우는 거예요. 건물 임대료 받으면서 건물주로서 안락한 노후를 보내는 거지.”

“건물주요?”

“간단히 말해서, 음. 그래. 저기 저 위 하늘에 있는 사람이라고 보면 돼.”

“아하.”

청풍이 감 잡았다는 듯 고개를 끄덕였다.

“무신(武神)이 되고 싶으신 거로군요.”

“아니, 그게 아니고. 거기서 무신이 왜 나와?”

“아닌가요?”

“아니지. 완전 달라.”

“하지만 무공은 좋아하시는 것 같은데.”

“내가? 딱히 그 정도까지는.”

“그런 것 치곤 표정이 좋으신데요.”

그 말을 듣고서야 깨달았다. 아까부터 시종일관 입꼬리가 올라가 있었다는 걸.

‘언제부터였지?’

잠시 생각에 잠긴 나를 향해 청풍이 싱긋 웃었다.

“숨도 다 고르셨으면 다시 시작할까요?”

“……언제부터 알고 있었어요?”

“제가 할아버지한테 많이 써먹은 방법이거든요.”

역시 사람 생각은 다 거기서 거기다. 난 풀썩 웃어 버렸다.

“생각보다 눈치가 빠르시네.”

“검은 더 빠르죠.”

츠츠츠.

청풍의 검신에서 자줏빛 검기가 쭉 솟구친 순간, 손안의 창이 거칠게 몸을 떨었다.



* * *



캉!

진가창법 일 초식. 곧게 뻗어 나간 창이 검신에 가로막혔다.

진가창법은 정직한 무공이다. 간결하고 투박하다. 분명 일류 무공이지만 묘리(妙理)로 따지자면 너무나도 단순하다.

‘화산파의 절기들에 비하면 턱없이 부족해.’

무공은 결국 동작들의 조합이다. 찌르고, 때리고, 베고. 공력의 운용, 미세한 각도 하나와 이어지는 초식으로 무궁무진한 변화를 만들 수 있다.

각고의 노력 끝에 마침내 대성을 이뤘지만 진가창법과 진가보법에는 그러한 묘리가 부족했다.

쐐애애애액! 타탕!

그런 의미에서 상대가 영 좋지 않다.

청풍은 내 무공을 단번에 꿰뚫어 볼 만한 눈을 가진 절정 고수다.

녀석은 더 이상 봐줄 생각이 없다는 듯이 본격적으로 몰아치기 시작했다.

쉬이이익! 파팟!

‘검법, 권법, 장공에 수공, 조공까지.’

녀석은 확실히 무공의 천재가 맞다. 어림잡아 열 가지는 되는 무공을 연계하면서도 움직임이 톱니바퀴처럼 딱딱 맞아떨어진다.

눈은 샛별처럼 빛나고 호흡은 느리고 안정되어 있다.

‘검성의 제자라 이거지.’

훌륭한 사부와 무공. 거기에 재능까지.

세상은 늘 불공평하다. 그리고 나는 지난 7년간 그 불공평한 세상에서 적응하는 법을 배웠다.

‘끈질기고 천천히. 결코 포기하는 법 없이.’

그게 내 방식이다.

저 멀리 앞서가는 토끼를 따라잡는 거북이가 되고 싶었던 건 아니었다. 결승선만 통과하면 그걸로 족했다.

살아남아 은퇴하는 것. 최하급 헌터가 꿀 수 있는 가장 큰 꿈이었다.

‘악착같이 살아남아야 했지.’

나는 게이트에서 모든 걸 배웠다. 녹슨 칼을 들고 독침을 쏘는 고블린들이 내 비무 상대였다.

무림의 비무와는 달리 목숨을 걸어야 하는 일이었지만 그렇기에 더 빨리 배울 수 있었다.

그리고…….

‘무림에 오게 됐지.’

차차차창! 서걱.

옆구리가 화끈하다. 피가 흐르는 것이 느껴졌어도 상처를 확인하는 멍청한 짓은 하지 않았다.

사람의 몸은 생각 이상으로 약하고, 한편으로는 강하다. 피가 좀 흐른다고는 해도 혈액이 응고되면 출혈은 곧 멎을 것이다.

“우욱!”

웃기게도 저 녀석이 비위가 약하다는 사실이 내게는 기회가 됐다.

나는 주춤하는 청풍을 향해 달려들었다.

‘진무창법 이 초식.’

쐐애애액!

무림에 떨어진 지 일주일쯤 됐을 때였나? 먼지 쌓인 서고에서 두 권의 비급을 발견했다. 진가창법과 진가보법.

왜 익혔냐고 물어보면 대답은 쉽다.

‘살아남기 위해서.’

내게 있어 무림은 또 하나의 게이트였다. 살아남기 위해서는 배워야 했다.

그렇게 무공에 입문했고, 어느덧 몇 달이라는 시간이 흘렀다. 그리고 모든 것이 송두리째 바뀌었다.

쉬쉬쉬쉭! 퍼벙!

‘흐읍.’

매화오품지. 다섯 줄기의 탄지공을 피하자마자 태을미리장을 얻어맞았다.

자그마치 100포인트를 쏟아부었건만 아직 청풍을 따라잡기에는 역부족이라는 뜻이다.

하지만 진가창법을 이미 속속들이 알고 있는 녀석을 상대하려면 무소의 뿔처럼 나아가는 수밖에 없다.

‘진가창법 삼 초식, 사 초식.’

진가창법은 나아갈수록 그 위력이 극대화된다. 보법도 그에 맞춰져 있다.

단순하지만 실전에 맞춰진 초식들로 상대를 압박하는 것. 그것이 내가 익힌 두 가지 무공의 본질이다.

‘이가 안 되면 잇몸으로.’

무공에 대한 이해도는 부족하지만, 능력치만큼은 결코 밀리지 않는다. 내가 전진하는 만큼 청풍은 물러났다.

흐름을 탄 나는 온 힘을 다해 창을 찌르고 베어 냈다. 입에서 단내가 풀풀 풍기는 와중에 문득, 방금 전 청풍과 했던 대화가 떠올랐다.



‘하지만 무공을 좋아하시잖아요?’

‘내가요? 딱히 그 정도까지는.’

‘그런데 왜 아까부터 웃고 계세요?’



그거야 당연히…….

‘재밌으니까.’

쐐애애액! 쾅!

검과 창이 격돌한다. 연무장 바닥에 가지런히 깔려 있던 청석이 가루가 되어 흩날렸다.

자욱한 먼지구름이 개이며 청풍의 모습이 보였다. 우리가 처한 상황과는 다르게 맑은 웃음이었다.

“무공, 재밌죠?”

잠시 고민하던 나는 말 없이 고개를 끄덕였다.

“아까는 왜 아니라고 했어요?”

“그냥…… 살아온 방식의 차이라고 해 둡시다.”

7년간 보이지 않는 뭔가에 쫓기는 듯 살았다.

죄책감, 혹은 책임감. 아니면 그 모든 걸 합리화시키기 위한 자기만족이라고 해도 좋다.

머뭇거리는 나를 보며 청풍이 입을 열었다.

“할아버지께서 언젠가 그런 말씀을 하셨어요. 무공? 그거 별거 없다!”

“음? 검성이?”

“진짜예요.”

억울한 표정을 한 청풍이 말을 이었다.

“무공(武功)이 아니라 무공(無空)이라고. 애초에 텅 비어 있으니 있는 그대로 받아들이고 채워 넣으면 된다고.”

“있는 그대로 받아들이고 채워 넣어라.”

“진짜라니까요? 나중에 할아버지한테 물어보실…….”

청풍의 목소리가 서서히 멀어지더니 이내 뚝 끊긴다.

나는 눈을 감았다. 캄캄한 어둠 속에서 시간의 흐름도, 장소도 잊은 채 뭔가에 사로잡힌 듯이 한 문장만 중얼거렸다.

‘있는 그대로 받아들이고 채워 넣어라…….’

왜 이 한 마디가 자꾸 마음에 걸릴까?

되새기면 되새길수록 심장이 방망이질치고 온몸이 근질거린다.

가슴에 내려앉은 바윗덩이가 들썩거리는 것 같았다.

‘무공(武功)이 아니라 무공(無空)이다. 있는 그대로 받아들이고 채워 넣어라…….’

몇 초, 아니 몇 시간이 흘렀는지도 모르겠다. 어둠 속에서는 시간의 흐름도 멈춘 듯했다.

하루, 이틀, 사흘, 설령 일 년이 흘렀다 해도 이상하지 않은 숨 막히는 어둠 속에서 나는 눈을 떴다.

“은인, 어떠세요?”

청풍의 물음에 대답하는 대신 주위를 둘러봤다.

혁무진은 저 구석에서 꾸벅꾸벅 졸고 있었고 먹빛 하늘은 금방이라도 쏟아질 듯한 별무리로 가득했다.

여기가 내가 알던 세상이 맞나?

“할아버지 말씀이 맞았나요?”

두 번째 물음. 나는 잔뜩 쉰 목소리로 대답했다.

“아뇨. 하나도.”

무공, 존나 어렵다.

그래도…….

띠링.



- 퀘스트, [벽을 넘어서]를 성공적으로 완료했습니다!

- [절정 고수]로 전직하셨습니다!



이제 하나는 알겠다.
```

## Final English reading copy

```markdown
# Chapter 159

Fifty points to Agility. And fifty points to Strength.

That made a hundred points in total. I had poured them all in at once—a massive number of points that would normally take ten Level-ups to earn—but I didn’t regret a single one.

*Points really are the best. Always thrilling. Always new.*

The toes kicking off the ground and the hand gripping the spear shaft cried out.

The me of now was far stronger than I had been only a few seconds ago.

And at last, I had taken the first step toward winning this duel.

*I’ll end this quickly.*

*Whoooooosh!*

The instant the spearhead came crashing down with a terrifying sound, a violet haze rose from Cheongpung’s entire body.

*The Zaha Divine Technique.*

It was proof that Cheongpung had finally begun fighting at full strength. But there was still one crucial thing left in this match.

*Whoooosh!*

As expected, a streak of Sword Energy shot up from Cheongpung’s waist.

Sword Energy, the exclusive domain of Peak masters, possessed enough cutting power to slice through steel.

I hadn’t yet crossed the wall into the Peak realm. I couldn’t meet it head-on.

I had to either retreat a step or factor in the spear being destroyed and continue with my next attack.

But…

*What is this feeling?*

A strange sense of déjà vu. My heart pounded, and my vision grew sharp. In a world that seemed to have slowed down, the cool spear shaft in my grip trembled.

*Vrrr. Vrrrr.*

Keep the head cool. Keep the heart hot.

That was how I had fought for seven years…but this time was different. This was instinct. Nothing but instinct ruled over my entire being.

*I can do it.*

Like a man possessed, I put more strength into the descending spearhead.

Forty-five years of internal energy raced along my fingertips toward the spearhead. The trembling in my grip grew stronger, and Cheongpung’s violet Sword Energy dazzled my eyes.

That was all.

*Boom!*

Two enormous forces collided.

A thunderous roar and brutal gusts of wind. Cheongpung’s eyes opened wide.

And then…

*It’s fine.*

The snow-white spearhead was still there.

The spearhead pressing down on Cheongpung’s Sword Energy trembled, not even a hairline crack running across it.

*Vrrrrrrr.*

It sounded like hundreds of bees beating their wings.

*How is this possible?*

Was this also the effect of raising my Strength? Or was it simply a coincidence?

At that moment, the answer to my question rang out.

> **System**
>
> - You have finished preparing to step into a new realm.
> - Your weapon is resonating with your energy.
> - Quest *Beyond the Wall* has been generated.

*Ah.*

It wasn’t the effect of raising my Strength. Nor was it a coincidence.

This was the natural order of things. After enduring countless hardships, I had finally come face-to-face with the wall. Now I had to cross it.

The wall of the Peak realm—a wall countless people had failed to overcome.

*A Peak master.*

True superhumans who wielded Sword Energy, or Aura.

A shiver ran through me at the thought alone. Memories from the past flashed before my eyes like a cheap monochrome film.

A mere F-rank Hunter, one of countless others, had made it this far. There had been countless crises, and someone had made a sacrifice.

> **System**
>
> **Quest:** *Beyond the Wall*
>
> Would you like to accept this Quest?
>
> **Y / N**

I had crossed the boundary between life and death countless times. I had to cross a mere Peak wall with ease if I didn’t want to be ashamed of the days I had lived through.

*Obviously yes.*

> **System**
>
> - You have accepted the Quest!

*Ding.*

As the cheerful System notification rang out, I pulled up the corners of my mouth.

My thoughts had been long, but only a short time had passed. I whispered to Cheongpung, who was looking up at me with bewildered eyes.

“Now, it’s Puramyeon spicy flavor.”[^3]

I’ll show you what Korean spice tastes like.

* * *

*Krrrnnng.*

Compared to roughly a minute ago, my Strength had risen by twenty-five percent.

It was the difference between heaven and earth. Cheongpung was visibly flustered by my sudden transformation.

“B-Benefactor. Where did this sudden strength come from?”

“It’s Korean rice power. Especially gukbap.”[^1]

“Pardon?”

“I used to eat two bowls of pork-bone hangover soup every morning. And five bowls of rice.”

“What does that even—gasp!”

*Krrrnnng.*

Cheongpung swallowed a breath as my force continued to build.

He had Sword Energy and the Zaha Divine Technique, but neither was having much effect. The spear, resonating while filled to the brim with my qi, had grown sturdy enough that even Sword Energy could no longer cut it.

*I have a real shot at winning.*

But Cheongpung was not an opponent who would go down easily.

“Hup!”

With a short shout, an incredible force knocked the spearhead upward.

It had only been lifted a handspan, but the instant Cheongpung escaped the pressure, he didn’t let the opportunity pass.

“I’m sorry. I took you far too lightly, Benefactor.”

Before he had even finished speaking, an invisible force shot from his palm.

The Taeeul Miri Palm. A secret ultimate technique of Huashan, personally taught to him by the Sword Saint himself.

“Hngh!”

*Bam-bam-bam!*

Sharp pain shot through me as I staggered backward five steps in succession.

Thank goodness I had improved my bones and muscles as well as my Sinews and Meridians with every Level-up. Otherwise, I would have been in serious trouble.

“Damn, that hurt.”

Cheongpung stared at me with the wide, startled eyes of a rabbit.

“A Seven-Star Taeeul Miri Palm…”[^2]

“Don’t say that. Now I want some cider.”

“Pardon?”

There it was. Exactly the reaction I expected.

The instant Cheongpung asked what I meant, my spear was already thrusting toward his chest.

A perfectly timed surprise attack. But there was no way it would end with just that.

As if answering my thoughts, Sword Energy slammed into the spearhead.

*Clang!*

*I wasn’t expecting it to work.*

With no expectations, there was no disappointment. And since my emotions remained steady, my forms did as well.

*Next, the waist.*

*Whoooosh!*

Cheongpung twisted his waist as the spear moved.

The gust raised by the spearhead silently sliced through his shirt. A faint line of blood appeared across the exposed flesh.

A small gain was still a gain.

*Next, the neck.*

I turned with the motion and swung the spear shaft at Cheongpung’s neck.

*Boom!*

That was not the sound that should have come from a collision between a human body and a steel spear.

But Cheongpung had martial arts—the Zaha Divine Technique, both one of the greatest internal-energy cultivation techniques under heaven and a protective qi art.

I clicked my tongue as I watched the violet energy around him grow denser.

*Even so, how can there be absolutely no damage? This is outright cheating.*

Talk about a plum-blossom silver spoon. How was I supposed to spar with this kind of unfair advantage?

But I didn’t have time to complain. Cheongpung had closed the distance to right in front of me in barely half a step, and the Sword Energy he scattered filled my vision.

*Whoooosh!*

The tip of his sword bloomed with flowers.

The movement was so fluid it was beautiful. But if I let myself be mesmerized, I would soon find myself standing before a sign for Mount Beimang.

The Plum Blossom Sword Technique I had watched until now was frightening martial arts—extremely intricate and complicated forms.

When Cheongpung wielded it, it felt as though I were trapped in a rainstorm.

But…

*I can see it.*

I opened my eyes wide. My breathing slowed, and my vision sharpened. The sound of my heartbeat was like thunder, and the spear trembled in my hands.

*Vrrrr. Vrrrrr.*

The spear was ringing.

At this moment, the spear and I were practically one body.

The spear shaft no longer felt cool.

*Shishishishik!*

Sword and spear became a blur.

I continuously deflected and knocked away the Sword Energy pouring down like rain.

Ten times, twenty, maybe thirty…

Cheongpung was tenacious and sharp beyond anyone I had ever fought.

When I countered the Sword Energy digging toward my waist, the Taeeul Miri Palm flew at me. When I avoided the Taeeul Miri Palm, the Crouching Tiger Fist aimed for my chest.

*Thud!*

The shoulder that blocked the Crouching Tiger Fist throbbed.

A momentary pain. As my movements slowed for an instant, Cheongpung opened the fist he had curled shut.

Air burst from the tips of his five fingers.

*Ah, damn it. Right, he had that too.*

The moment I realized it, I bent my waist backward like a bow.

The Plum Blossom Five-Point Finger. He had shown it only once during his duel with Jin Mukyung.

*Pip-pip-pit!*

Five streams of finger force grazed the bridge of my nose and earlobe by a hair.

*He really is strong.*

I felt it again: Cheongpung was not an ordinary swordsman.

He was not only the heir of the Sword Saint Mae Jonghak. He had also mastered Huashan’s secret techniques—in other words, he was a complete gift set of Huashan martial arts.

I wiped away the blood seeping from my wounds and spoke.

“You’re coming on a little strong, aren’t you?”

“That’s what I’d like to say to you, Benefactor. Honestly, you surprised me.”

“Why? Because someone who seemed like no big deal is fighting much better than expected?”

“Yes!”

“…”

“You’re better than I thought. Seriously. And…”

“And?”

“It’s fun.”

As I watched the faint smile on Cheongpung’s lips, I thought about it.

Setting his competitive pride aside, this guy simply loved martial arts themselves. He was proving to me how frightening a genius who truly enjoyed martial arts could be.

“Aren’t you the same as me, Benefactor?”

“Young Hero Cheong, do you know what my dream is?”

“…”

“To retire in one piece and put up a building in my name. I’ll collect rent and spend my old age in comfort as a landlord.”

“A landlord?”

“Put simply, um… Yes. You can think of it as being one of those people up in the sky.”

“Ah-ha.”

Cheongpung nodded as though he understood.

“You want to become the Martial God.”

“No, that’s not what I meant. Where did the Martial God come from?”

“Is that not it?”

“No. It’s completely different.”

“But you do seem to like martial arts.”

“Me? Not to that extent.”

“Your expression looks happy.”

Only then did I realize that the corners of my mouth had been raised the entire time.

*Since when?*

As I stood lost in thought, Cheongpung smiled brightly.

“If you’ve caught your breath, shall we start again?”

“…How long have you known?”

“It’s a method I’ve used on my grandfather many times.”

People really were all alike. I burst out laughing.

“You’re more perceptive than I expected.”

“My sword is faster.”

*Tsssss.*

The moment violet Sword Energy surged from Cheongpung’s blade, the spear in my hands trembled violently.

* * *

*Clang!*

The First Form of the Jin Family’s Spear Technique. The spear thrust straight ahead was blocked by the sword blade.

The Jin Family’s Spear Technique was an honest martial art. Simple and rough.

It was clearly a First Rate martial art, but when it came to subtle principles, it was far too simple.

*Compared to Huashan’s secret techniques, it falls hopelessly short.*

Martial arts ultimately came down to combinations of movements.

Thrust, strike, cut.

Through the circulation of internal energy, the slightest change in angle, and the forms that followed one another, one could create endless variations.

I had attained mastery after arduous effort, but the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique lacked that kind of subtlety.

*Whoooooosh! Clang!*

In that respect, my opponent was a terrible match for me.

Cheongpung was a Peak master with eyes sharp enough to see through my martial arts at a glance.

As if he had decided to stop holding back, he began pressing the attack in earnest.

*Whoosh! Bam-bam!*

*Sword techniques, fist techniques, palm techniques, hand techniques, even claw techniques.*

He really was a genius of martial arts. He chained together roughly ten different martial arts, yet every movement fit perfectly into the next, like interlocking gears.

His eyes shone like morning stars, and his breathing was slow and steady.

*So this is what it means to be the Sword Saint’s Disciple.*

An excellent Master and excellent martial arts.

And talent on top of that.

The world was always unfair. And over the past seven years, I had learned how to adapt to that unfair world.

*Persist, move slowly, and never give up.*

That was my way.

I had never wanted to be a tortoise that caught up with a rabbit far ahead.

Crossing the finish line was enough.

Surviving and retiring. That was the greatest dream a lowest-rank Hunter could have.

*I had to claw my way to survival.*

I learned everything in the Gates. Goblins holding rusty knives and firing poison needles were my sparring partners.

Unlike duels in the Murim, I had to stake my life on every fight. But that was why I learned faster.

And then…

*I came to the Murim.*

*Clang-clang-clang! Slash!*

My side burned. I could feel blood flowing, but I didn’t make the stupid mistake of checking the wound.

The human body was weaker than you might think, and stronger in its own way. Even if some blood was flowing, the bleeding would soon stop once it clotted.

“Ugh!”

Funny enough, Cheongpung’s weak stomach gave me an opening.

I charged at the Cheongpung who had faltered.

*Second Form of the Jin Family’s Spear Technique.*

*Whoooooosh!*

It had been about a week after I fell into the Murim, I think.

I found two martial arts manuals in a dust-covered archive: the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

If you asked why I learned them, the answer was simple.

*To survive.*

To me, the Murim was another Gate.

I had to learn if I wanted to survive.

That was how I entered the world of martial arts. Before I knew it, several months had passed.

And then everything changed completely.

*Shishishishik! Bam!*

*Hngh.*

The Plum Blossom Five-Point Finger.

The instant I avoided the five streams of finger force, the Taeeul Miri Palm struck me.

I had poured in a full hundred points, but I still hadn’t caught up to Cheongpung.

However, to fight someone who already knew the Jin Family’s Spear Technique inside and out, I had no choice but to keep charging forward like a rhino.

*Third Form of the Jin Family’s Spear Technique. Fourth Form.*

The Jin Family’s Spear Technique grew more powerful the farther it advanced. Its footwork was designed to match.

Its essence was to pressure an opponent with simple forms tailored for actual combat.

*If I can’t do it with my teeth, I’ll do it with my gums.*

My understanding of martial arts might be lacking, but my stats were not inferior.

As I pressed forward, Cheongpung retreated.

Riding the momentum, I thrust and slashed with all my strength. Even as I panted until my mouth tasted sweet, I suddenly remembered the conversation I had just had with Cheongpung.

*But you like martial arts, don’t you?*

*Me? Not to that extent.*

*Then why have you been smiling?*

That was obviously because…

*It’s fun.*

*Whoooooosh! Boom!*

Sword and spear collided.

The bluestone laid neatly across the training ground shattered into powder and scattered through the air.

As the thick cloud of dust cleared, Cheongpung came into view.

His smile was clear and bright, completely at odds with the situation we were in.

“Martial arts are fun, right?”

After thinking for a moment, I nodded without a word.

“Why did you say they weren’t earlier?”

“Let’s just call it a difference in how we’ve lived.”

For seven years, I had lived as though I were being chased by something invisible.

Guilt, perhaps. Or a sense of responsibility.

Or maybe it was simply self-satisfaction, a way to rationalize all of it.

As he watched me hesitate, Cheongpung spoke.

“My grandfather once told me something. He said, ‘Martial arts? They’re nothing special!’”

“Hmm? The Sword Saint?”

“It’s true.”

Cheongpung continued with an aggrieved expression.

“He said it wasn’t martial arts, but empty space[^4]. Since it’s empty to begin with, you just accept it as it is and fill it in.”

“Accept it as it is and fill it in.”

“I’m serious. You can ask my grandfather later…”

Cheongpung’s voice gradually faded, then cut off completely.

I closed my eyes.

In the pitch-black darkness, forgetting the passage of time and the place I was in, I muttered a single sentence as though possessed.

*Accept it as it is and fill it in…*

Why did those words keep catching at my heart?

The more I repeated them, the harder my heart pounded and the more my entire body itched.

It felt as though the boulder weighing down my chest were shifting.

*It isn’t martial arts. It’s empty space. Accept it as it is and fill it in…*

I didn’t know whether several seconds or several hours passed.

In the darkness, even the flow of time seemed to have stopped.

In that suffocating darkness, where it would not have been strange for a day, two days, three days, or even a year to pass, I opened my eyes.

“Benefactor, how do you feel?”

Instead of answering Cheongpung’s question, I looked around.

Hyuk Mujin was dozing in the corner, while the ink-dark sky was filled with a cluster of stars that looked ready to pour down at any moment.

Was this really the world I knew?

“Was my grandfather right?”

It was Cheongpung’s second question.

I answered in a hoarse voice.

“No. Not at all.”

Martial arts were fucking hard.

Still…

*Ding.*

> **System**
>
> - Quest *Beyond the Wall* has been successfully completed!
> - Your class has changed to **Peak Master**!

Now I knew one thing.

[^1]: *Gukbap* is soup served with rice; *bone haejangguk* is a hearty pork-bone soup traditionally eaten as hangover food.

[^2]: The Korean word for “seven-star” also appears in *Chilsung Cider*, a Korean lemon-lime soft drink, setting up Taekyung’s next line.

[^3]: Puramyeon is an instant-noodle brand. Taekyung uses its spicy flavor as the next step in his escalating flavor joke.

[^4]: Mae’s line is a wordplay on two Korean terms pronounced *mugong*: “martial arts” and “empty space.”
```
