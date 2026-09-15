<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0162.txt",
      "sha256": "c7d5e57f7143bfa49b0b9bf7bdff2cac7cbfdb0b754e1a4b8e1622c776d6bb23",
      "bytes": 15186
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f142ef05a16a0e224ff2bc4c8a7f4d6e8f4c486112ac8c9d92627079a2fa25a4",
      "bytes": 8079
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "22fa0a019eed745d68d3b46d562b6d1968227dd9b1cdfb191f8c8fc22a4fe4df",
      "bytes": 39793
    },
    {
      "path": "characters/Black Sand.md",
      "sha256": "c8e81dc4452c2ea3e6eb54ac7b9fa449028d3620fef52fd7780caa5638021cd7",
      "bytes": 865
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "c0020f0950d896bcd03919b488fe24b53d42659fceacb6b7dee90a878f91c351",
      "bytes": 611
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "93aec7fc37aa2ccd9fbe3e9b2ce766e6bafc5299daa89053065f568b17d9580b",
      "bytes": 599
    },
    {
      "path": "characters/Temur.md",
      "sha256": "e6ce75332d8fa43301d4fa40ec1d5b6a448125db8a23445f9648c718459fc74c",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3dd84a9df70d77d64d03013dd541585b2c591c3728499d02ba2ffaf3ebedf04e",
      "bytes": 31272
    }
  ],
  "estimated_tokens": 29329
}
-->

# Durable State Update — Chapter 162

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 162. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 162. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 162,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 162,
    "continuity_sources": [162],
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
    "The City Lord's luncheon requirement concluded with Prince Shangshan's Token obtained as the Quest Reward; Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days. Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung completed Beyond the Wall after spending 50 points on Agility and 50 on Strength; the System changed his class to Peak Master, and his weapon resonated with his energy.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is twenty years old, a Peak master raised by Mae Jonghak, knows numerous Huashan martial arts, can use the Zaha Divine Technique and Sword Energy, has no martial title, and teaches Taekyung and Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence for at least ten years; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is Huashan's Lone Crane and the first of the Three Plum Blossom Elites; Chulwoo and Eunhyang are his junior disciples and fellow Elites, and all three are traveling to meet Cheongpung again.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk; the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served him since infancy, and is the power behind the Shanxi Provincial Office.",
    "Jin Mukyung lost to Cheongpung four days before the luncheon, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Jin Wikyung is the thirty-five-year-old Lesser Family Head and future Family Head, directing the Jin Family's expansion and branch stabilization while aiming to establish it as a great family.",
    "Taekyung previously failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Taekyung has a private training ground in a rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung, and their Wall Lizard Technique training is complete.",
    "Wipeng offered to personally lead useful martial artists against approximately five hundred mounted bandits gathering near Datong; Huashan sent the Three Plum Blossom Elites and reported Mae Jonghak missing.",
    "Cheongpung canceled the second Sword Saint-training Quest by his own decision without penalty, postponing the unfinished duel with Taekyung.",
    "Cheongpung had only ever sparred with Mae Jonghak before leaving Huashan and is adjusting with difficulty to fighting people outside his grandfather's instruction; he considers Taekyung and Jin Mukyung the strongest people he has met since leaving Huashan.",
    "Cheongpung identifies Taekyung's rough, unrefined martial arts and naturally emerging aura as Wildness; Taekyung can increasingly read and imitate Cheongpung's forms during sparring.",
    "Hyuk Mujin has resolved to become strong enough to be remembered as Jin Taekyung's right arm or heart and by the name Hyuk Mujin; he is now Level 50 after recent training and sparring.",
    "Taekyung's Peak breakthrough completed Beyond the Wall, changed his class to Peak Master, raised Jin Family's Cultivation Technique to the ninth stage and Qi Sense to the seventh stage, unlocked trainable Sound Transmission, and awarded Ten-Thousand-Year Cold Iron plus the Find the Craftsman Quest.",
    "Black Sand, the Human Butcher, Temur, and Chinggen are described as exceptional Peak masters. Black Sand commands the Black Sand Band and the subordinate Heavenly Wind Band, and has formed a four-way alliance with the other three to attack the Jin Family of Taiyuan through Hequ on New Year's Day."
  ],
  "continuity_sources": [
    161
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him, and did he actually go to the Jin Family after breaking seclusion to find Cheongpung?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?"
  ],
  "safe_through": 161,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally; render 초일류 as “advanced First Rate,” 군문 as “military,” 풍운검군 as “Wind-and-Cloud Sword Lord,” and 오촌 당숙 as “father's cousin.”",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” 광염 as “light-flames,” 검명 as “Sword Cry,” and 창명 as “Spear Cry.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” 환골탈태 as “Bone Transformation,” and 전음 as “Sound Transmission.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 태초 마을 as “Taecho Village,” 벽호공 as “Wall Lizard Technique,” 낙안봉 as “Falling Goose Peak,” 대초원 as “Great Steppe,” 마유주 as “mare's-milk wine,” 게르 as “ger,” and 북부 고원 as “Northern Gaoyuan.”",
    "Render 황하방 as “Yellow River Gang,” 소공문 as “Sogong Sect,” 남부상회 as “Southern Merchant Guild,” 내당주 as “Inner Hall Master,” 내외당 as “Inner and Outer Halls,” 세가 as “great family,” and 한족 as “Han Chinese.”",
    "Render 암향표 as “Dark Fragrance Drift,” 복호권 as “Crouching Tiger Fist,” 천근추 as “Thousand-Catty Drop,” 야성 as “Wildness,” 오행매화보 as “Five-Element Plum Blossom Steps,” 공수납백인 as “Empty-Hand Seizes the Blade,” 매화오품지 as “Plum Blossom Five-Point Finger,” 벽을 넘어서 as “Beyond the Wall,” and 절정 고수 as “Peak Master.”",
    "Retain Taekyung's instant-noodle flavor joke with “mild Neoguri,” “Jin Ramen spicy flavor,” and “Puramyeon spicy flavor”; render 천근거력 as “the force to move a thousand catties,” 인도 as “Human Butcher,” 대칸 as “Great Khan,” 텡게르 as “Tengger,” and preserve the 무공/무공 wordplay as “martial arts” and “empty space.”",
    "Render 흑사 as “Black Sand,” 흑사대 as “Black Sand Band,” 천풍단 as “Heavenly Wind Band,” 천풍단주 as “Heavenly Wind Band Leader,” and 하곡 as “Hequ.”"
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
| 매화오품지 | **Plum Blossom Five-Point Finger** | Five-finger technique Cheongpung uses during the duel. |
| 벽을 넘어서 | **Beyond the Wall** | System Quest generated during Taekyung's breakthrough. |
| 절정 고수 | **Peak Master** | System class awarded after Taekyung completes Beyond the Wall. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 텡게르 | **Tengger** | Sky deity invoked by Temur. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |
| 천풍단 | **Heavenly Wind Band** | Five-hundred-member northern plateau mounted-bandit force subordinate to Black Sand. |
| 천풍단주 | **Heavenly Wind Band Leader** | Leader operating under Black Sand's orders near Datong. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |

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
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 인도 | 흑사 | rival_power_to_rival_power | Black Sand | blunt and familiar | Uses 흑사 while cutting off Black Sand's joking introduction. |
| 흑사 | 인도 | rival_power_to_rival_power | you | playful and taunting | Teases the Human Butcher about being called a butcher without showing fear. |
| 흑사 | 칭겐 | alliance_recruiter_to_recruited_chieftain | Chinggen | lightly teasing and probing | Identifies Chinggen by name while commenting on his composure and perceptiveness. |

## Exact glossary matches

| 무림     | **Murim**          |
| 하오문    | **Lower District Sect**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |

## Listed compact profiles

### Black Sand.md

# Black Sand (흑사)

- **Safe through:** Chapter 161
- **Aliases:** None
- **Role:** Leader of the Black Sand Band, a Han-Chinese mounted-bandit power of one hundred; secretly commands the five-hundred-member Heavenly Wind Band through its leader and organizes the planned attack on the Jin Family of Taiyuan
- **Personality:** Frivolous and warm on the surface but calculating, bold, authoritative, and adept at manipulating dangerous people through humor and grand promises
- **Voice:** Light, teasing, and conversational in ordinary speech; becomes firm and decisive when directing the alliance
- **Relationships:** Commands the Black Sand Band and the subordinate Heavenly Wind Band; recruited the Human Butcher, Temur, and Chinggen into a four-way alliance against the Jin Family of Taiyuan

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 161
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his fellow chieftain, and Chinggen repeatedly restrains Temur's recklessness; Black Sand recruited both chieftains into a four-way alliance to attack the Jin Family of Taiyuan

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 161
- **Aliases:** None
- **Role:** Mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 161
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and hostile to Han Chinese encroachment
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his fellow chieftain and restrains him from provoking the Human Butcher; both chieftains accepted Black Sand's proposal for a four-way alliance to attack the Jin Family of Taiyuan

## Korean source

```text
＃162화



그런 순간이 있다. 시끌벅적하고 빈틈없이 맞물린 소음이 갑자기 사라지는 순간이. 지금이 바로 그랬다.

끼이이이익.

낡은 문이 열리는 소리에 소란스럽던 객잔 안이 조용해졌다.

산서성을 발칵 뒤집어 놓을 계획을 세우고 축배를 들던 네 명의 우두머리와 이백여 명에 이르는 마적, 유목민들의 시선이 모두 입구를 향해 쏠렸다.

저벅. 저벅. 저벅.

‘저건…….’

천천히 자신들을 향해 걸어오는 불청객을 확인한 흑사(黑蛇)의 눈이 가늘어졌다.

‘웬 노인네야?’

불청객의 정체는 노인(老人). 말 그대로 늙은 사람이다.

그러나 흑사는 지금 다가오는 저 노인보다 늙은 사람을 본 적이 없었다.

‘거의 시체 수준이군.’

금방이라도 쓰러질 듯 비틀거리는 걸음걸이, 쭈글쭈글한 피부는 꽁꽁 얼어 있었고 내뱉는 숨은 가늘기만 했다.

가만히 노인을 지켜보던 테무르와 칭겐, 인도가 대화를 주고받았다.

“저 정도로 늙은 사람은 처음 보는군. 우리 부족의 주술사보다 더 늙었어.”

“그런데 웬 늙은이지? 행색은 또 왜 저렇고?”

“마적이라도 만났나 보지.”

말마따나 노인의 행색은 초라하기 그지없었다. 어디서 낭패라도 당했는지 걸치고 있는 옷은 너덜너덜했고, 살가죽만 남은 몸뚱어리가 훤히 보였다.

“재수도 없는 늙은이군. 기껏 살아남아 온 곳이 마적 소굴이니.”

인도가 혀를 찼다.

“저런 늙은이는 죽이고 싶은 마음도 안 든다. 치워라.”

“옛.”

인도의 수하가 나서려던 그때였다.

“잠깐.”

손을 들어 제지한 사람은 흑사였다. 노인을 응시하는 그의 미간이 좁아졌다.

‘뭔가 이상하다.’

그들이 머물고 있는 이 객잔은 마적들에 의해 만들어졌다. 때문에 주인, 숙수, 점소이도 모두 마적이거나 마적 출신이다.

북부 고원 유일의 중립지이기 때문에 오늘 같은 화합이나 화해의 장이 되기도 했다.

‘그런데 이런 곳에 제 발로 기어와? 그것도 저런 늙은이가?’

북부 고원에 발을 디딘 자라면 객잔의 존재 또한 당연히 안다.

평범한 양민이 출입했다가는 죽은 목숨이라는 사실도.

“왜 그러시오?”

“쉿, 잠시 기다리게. 어째 심상치 않아.”

흑사의 반응에 다른 이들도 문득 이상함을 느끼기 시작했다.

“그러고 보니 여긴 어떻게 왔지?”

“외지인 같은데…….”

“외지인은 아니다. 저런 늙은이가 몸 성히 여기까지 왔을 리 없어.”

북부 고원에는 수백 개의 마적단과 유목 부족이 흩어져 있다. 어지간히 간덩이가 붓지 않고서야 혈혈단신의 몸으로 고원을 가로지를 생각은 하지 못한다.

흑사를 포함한 네 사람은 각자 생각에 잠겼다.

‘혹시……?’

‘무림인이라면 가능하지.’

‘무림인? 저 노인네가?’

‘신경 쓰인다. 죽여야겠어.’

특히나 인도에게 살인이란 숨 쉬는 것과 별반 다를 바가 없다. 거침없이 검갑에 손을 가져가는 그를 흑사가 노려봤다.

이어 인도의 귓가를 파고드는 한 줄기 전음.

- 기다리라고 했네. 좀 더 지켜본 후에 움직여도 늦지 않아. 무림에서는 여자와 아이, 노인을 조심하라는 말도 못 들어 봤나?

- 걱정도 유분수군. 저런 비루먹은 늙은이가?

- 경거망동하지 말게. 무림에서는 어떤 일이 벌어질지 몰라.

툭 치면 죽을 것 같은 늙은이다. 그러나 흑사의 경고를 무시할 수도 없었다.

인도가 짜증 섞인 한숨과 함께 검갑을 내려놨다.

- 잘 생각했네.

그사이 정체불명의 노인은 후들거리는 발걸음으로 네 사람의 앞까지 도달해 있었다.

묘한 긴장감이 흐르는 가운데, 흐릿한 눈빛으로 주위를 둘러본 노인이 입을 열었다.

“무, 물 좀…….”

물을 찾는 바짝 마른 목소리에 사람들이 그럼 그렇지, 하는 얼굴로 고개를 저었다.

하지만 흑사만큼은 달랐다. 치밀하고 용의주도한 성격인 그는 마지막까지 경계를 풀지 않았다.

“노인장께서 목이 타시는 모양이다. 시원한 물을 가져다드려라.”

“존명.”

마적에게서 잔을 건네받은 노인이 허겁지겁 물을 들이켰다. 어찌나 급하게 마시는지 저러다가 쓰러지지는 않을까 걱정이 될 정도였다.

노인은 연거푸 대여섯 잔을 들이켜고 나서야 고개를 들었다.

“후우.”

“이제 좀 괜찮으시오?”

노인의 쭈글쭈글한 얼굴 위로 함박웃음이 번졌다.

“네!”

“……?”

“감사합니다, 아저씨!”

아저씨라니? 당황한 흑사가 벌떡 일어나 노인의 손목을 잡아챘다.

아무런 저항도, 힘도 없다. 앙상한 뼈는 조금이라도 힘을 주면 부러질 것 같았다.

“이보시오, 노인장?”

“네? 왜요?”

어린아이 같은 웃음과 말투. 노인을 물끄러미 바라보던 흑사의 얼굴이 일그러졌다.

“젠장. 정신 나간 노인네로군.”

맥이 탁 풀렸다. 분명히 뭔가 이상한 느낌을 받았는데…… 전부 기분 탓이었던 모양이다.

아무래도 큰일을 앞두고 있다 보니 신경이 곤두설 수밖에 없었다.

고개를 절레절레 흔드는 흑사를 인도가 비웃었다.

“무림에서는 어떤 일이 벌어질지 모른다더니. 그 말이 꼭 맞았군. 노환(老患)에 시달리는 노인이라니. 크하하!”

“그 주둥이 닥치게.”

퉁명스럽게 대꾸한 흑사가 노인의 손목을 놓으려던 그때였다.

“여긴 또 어디여?”

아까와는 전혀 다른 카랑카랑한 목소리. 어느새 또렷해진 눈빛으로 사방을 둘러본 노인이 한숨을 푹 내쉬었다.

“염병할. 늙으면 죽어야지.”

척 보아하니 이제야 제정신으로 돌아온 모양. 노인의 푸념에 곳곳에서 웃음이 새어 나왔다.

완전히 여유를 되찾은 흑사도 피식 웃으며 물었다.

“노인장, 이제 정신이 드시오?”

노인이 대답했다.

“어린노무 새끼가 어디서 하오체야? 하오문 출신이냐?”

“……어?”

“손목은 또 왜 잡고 있어? 나랑 정분나고 싶어?”

“이, 이보시오.”

“놔, 안 놔? 셋 센다. 하나, 둘, 셋.”

휙. 엉겁결에 손목을 놔 버린 흑사는 갑작스러운 상황에 정신이 하나도 없었다.

‘이 늙은이, 도대체 뭐지?’

걸쭉한 욕설, 다다다 쏘아붙이는 말에 저절로 몸이 움직였다.

분명 무공 한 줄 모르는 정신 나간 노인에 불과한데…… 귀신에라도 홀린 기분이었다.

“크하하하! 아주 제대로 당했군!”

인도가 광소를 터트렸다. 안 그래도 무공으로 치자면 한 수 아래인 흑사가 대장 노릇을 하던 것이 마음에 안 들던 차였다.

그런 상황에서 흑사가 정신이 오락가락하는 늙은이에게 망신당하는 걸 보니 속이 다 후련했다.

“늙은이가 입담이 아주 제법이군. 덕분에 크게 웃었으니 살려 줘야겠어.”

하지만 인도의 입가에 걸린 흡족한 미소가 사라지기까지는 그리 오랜 시간이 필요하지 않았다.

노인의 입에서 튀어나온 한마디 때문이었다.

“이런 호래자식이…… 넌 애미 애비도 없냐?”

“……!”

순간 객잔 안이 싸늘한 침묵에 잠겼다.

흑사와 인도가 누구인가. 북부 고원을 주름잡는 거물들이다. 세력도 세력이지만 스스로도 어지간한 마적단 하나를 우습게 박살 내는 절정 고수들.

존경과 두려움을 한 몸에 받는 두 사람을 노인은 말 몇 마디로 난도질해 버렸다.

“한 놈은 하오문 출신 남색가고, 한 놈은 부모도 없이 자라서 혓바닥이 반 토막 난 놈. 그리고 나머지 두 놈은……”

변발을 한 테무르와 칭겐을 슬쩍 바라본 노인이 한숨을 내쉬었다.

“젊은 놈들이 벌써부터 이마가 다 까졌군. 불쌍한지고.”

이제는 더 이상 놀랄 기력도 없다. 충격과 공포에 휩싸인 분위기 속, 쯧쯧 혀를 찬 노인이 네 사람 앞에 놓인 음식을 발견하고 눈을 크게 떴다.

“아따, 한 상 우라지게 차려 놨네. 배고팠는데 잘됐다.”

누가 말릴 새도 없었다.

잘 구워진 오리 한 마리를 집어 든 노인이 다리를 잡고 북 뜯었다.

“햐, 살코기 야들야들한 것 보소. 아주 혀에서 살살 녹는다, 녹아.”

우걱우걱.

다리 두 쪽을 게 눈 감추듯 해치운 노인이 분노와 충격으로 몸을 부르르 떨고 있는 인도에게 대뜸 살점을 쓱 내밀었다.

“아직 젊은 놈이 왜 이렇게 몸을 떨어 대? 몸이 허해서 골골거리지 말고 이거나 먹어. 나는 퍽퍽한 가슴살은 싫, 아니 못 먹어. 이가 안 좋아서.”

뚜둑.

객잔에 있던 모든 사람이 같은 소리를 들었다.

그건 인도의 마지막 이성의 끈이 끊어지는 소리였고, 한 사람의 죽음을 예고하는 단말마였다.

“이 개 같은 늙은이가!”

다음 순간, 눈이 뒤집힌 인도의 신형이 번개처럼 솟구쳤다. 동시에 그의 손에 들린 참마검(斬馬劍)에서 줄기줄기 쏟아진 핏빛 검기가 전방을 휩쓸었다.

“이런 미친!”

“피해!”

콰과광!

테무르와 칭겐이 몸을 빼기 무섭게 굉음이 터져 나왔다.

수백, 수천 개의 나무 조각이 사방으로 튀었고 먼지 구름이 휘몰아쳤다.

“죽어! 죽어! 죽어!”

그 광경을 지켜보던 이들은 모골이 송연해졌다. 지금 인도에게서 느껴지는 광기를 보건대, 노인은 육편(肉片) 하나 남기지 못하고 죽었을 게 뻔했다.

“정신 나간 늙은이가 감히! 크아아악!”

콰과과광!

쉼 없이 쏟아지는 검기의 향연. 마침내 인도가 참마검을 거둬들인 것은 일다경이 지난 후였다.

“후우, 후우…….”

거친 숨을 몰아쉬던 인도가 허공에 검을 휘둘렀다. 그러자 검압에 의해 먼지구름이 흩어지며 반쯤 가루가 된 폐허가 모습을 드러냈다.

모두의 짐작처럼 노인은 그 어디에도 보이지 않았다.

“내가 본 가장 용감한 사람이었어.”

“노인장, 잘 가시오.”

“그러니까 어쩌자고 인도를 건드려서…….”

“역시 한족 놈들, 엄청나게 포악하군.”

이백여 명의 마적과 유목민들이 작은 목소리로 수군거리던 그때였다.

우적우적. 꿀꺽. 크허!

“……?”

“……?”

“……?”

처음에 느낀 것은 황당함이었다. 이 분위기 속에서 어떤 눈치 없는 놈이 음식과 술을 먹는단 말인가.

그러나 물음표가 느낌표로, 황당함이 경악으로 바뀌는 데까지는 촌각이면 충분했다.

“느, 늙은이! 늙은이가 살아 있다!”

“뭣이! 어디?”

“뒤다! 뒤에서 들렸어!”

누군가의 외침. 그리고 모두가 귀를 의심케 할 카랑카랑한 목소리가 이어졌다.

“요즘 놈들은 참 싸가지가 없어서 문제야. 내 이름이 늙은이냐? 네 친구야?”

“어어, 어어어!”

“안 되겠다. 오늘 네놈들 버르장머리를 단단히 고쳐 주마.”

퍼버버벅! 부웅!

객잔을 가득 메우고 있던 마적과 유목민들이 휙휙 날아올랐다.

하나같이 사지가 으스러지고 안면이 박살 난 상태로 튕겨 나가는 광경에 우두머리들은 식은땀을 흘렸다.

‘이, 이게 무슨.’

‘도대체 어떻게 저기에 있는 거지?’

‘움직이는 것을 보지도 못했다.’

고수.

그것도 절정 고수인 자신들의 눈을 속일 정도의 고수다.

흑사, 테무르, 칭겐이 딱딱하게 굳어 버린 그때, 유일하게 한 사람만이 노인을 향해 돌진했다.

“이 개 같은 늙은이가!”

이미 눈이 뒤집힌 인도는 거리낄 것이 없었다. 거칠게 쇄도하는 그를 확인한 노인이 눈살을 찌푸렸다.

“너는…….”

“그래, 나다! 이번에는 반드시 죽여 주마!”

“부모 없는 놈이로구나.”

“크아아악!”

쐐애애애액!

태산압정. 핏빛 검기가 활활 타오르는 참마도가 노인의 정수리를 쪼개려던 그 순간. 노인이 뭔가를 휘둘렀다.

서걱! 쿵!

시간이 정지한 것 같았다. 숨소리 하나 들리지 않는 침묵 속, 모두가 자신의 눈을 의심했다.

반 토막이 난 참마검, 그리고 노인의 손에 들린 자그마한 무언가.

“이, 이건…….”

인도의 눈빛이 처음으로 안정을 되찾았다. 그는 두려움과 경악 어린 시선으로 노인을 바라봤다.

“……닭 뼈?”

“닭은 버릴 곳이 없지. 맛도 좋고, 뼈는 푹 고아 먹고. 가끔은 검기도 쓰고.”

닭 뼈로 검기를 쓰다니. 이런 괴이한 광경은 어디에서 본 적도, 들은 적도 없다.

인도는 직감했다.

‘고수. 초절정 고수다. 결코 대적할 수 없는.’

노인은 충격에 빠진 인도를 보며 중얼거렸다.

“그나저나…… 흉악한 놈이로고. 온몸에서 피 냄새가 진동을 하는구나.”

한마디, 한마디에 소름이 돋는다. 일평생을 포식자로 살았건만, 지금은 호랑이 앞의 쥐새끼나 다름없다.

“이런 놈은 가만히 놔두면 안 되는데…….”

인도는 문득 오한을 느꼈다. 노인의 전신에서 흘러나오는 죽음의 기운에 이빨이 딱딱 부딪쳤다.

“제, 제발.”

“응?”

“제발 살려 주십시오. 제발…….”

뺨을 타고 눈물이 흘렀다. 바지는 축축하게 젖었고 힘이 풀린 손아귀에서 참마검이 미끄러졌다.

평생 남의 목숨을 빼앗아 왔던 인간 백정의 애원. 그 누구도 믿을 수 없는 광경이었다.

그런 그를 물끄러미 바라보던 노인이 입을 뗐다.

“두려워하지 말거라.”

됐다, 살았다! 죽음의 위기에서 벗어났다!

인도가 자신도 모르게 안도의 한숨을 내쉬던 그때였다.

턱.

뼈마디가 튀어나와 있는 손. 거칠고 주름진 노인의 손이 그의 가슴을 짚었다. 그리고 그것이 마지막이었다.

“……아?”

미약한 의문과 함께 세상이 뒤집혔다. 쓰러진 그의 칠공(七空)에서 흘러나온 피가 바닥을 적셨다.

‘살려 준다면서, 왜?’

흐릿해지는 시야, 멀어지는 소음 너머로 노인의 한마디가 들려왔다.

“두려워하지 마라. 고통 없이 보내 줄 테니.”

노인의 말이 맞았다. 고통은 없었다.



* * *



인도.

중원까지 흉명을 떨친 절정 고수가 고작 일수(一手)에 명을 달리했다.

“자, 그래서…….”

얼어붙은 사람들을 향해 노인이 입을 뗐다.

“여기가 어디냐?”
```

## Final English reading copy

```markdown
# Chapter 162

There are moments when the boisterous, perfectly interlocking din of a place suddenly disappears.

This was one of them.

*Creeeeak.*

The inn fell silent at the sound of its old door opening.

The gazes of the four leaders and more than two hundred mounted bandits and nomads, who had been raising their cups in celebration of their plan to turn Shanxi Province upside down, all converged on the entrance.

*Step. Step. Step.*

*What the…?*

Black Sand’s eyes narrowed as he identified the uninvited guest slowly walking toward them.

*What’s with this old man?*

The uninvited guest was an old man. Literally an old man.

But Black Sand had never seen anyone older than the man approaching them now.

*He’s practically a corpse.*

His unsteady gait made him look as though he could collapse at any moment. His wrinkled skin was ice-cold, and the breath escaping his lips was thin and faint.

Temur, Chinggen, and the Human Butcher watched the old man in silence for a while before exchanging a few words.

“That’s the oldest person I’ve ever seen. He’s older than our tribe’s shaman.”

“But what’s an old man doing here? And why is he dressed like that?”

“He must have run into some mounted bandits.”

As they said, the old man’s appearance was utterly miserable. His clothes were tattered, as though he had suffered some misfortune somewhere, and his body was so emaciated that only skin seemed to remain.

“What an unlucky old man. After barely surviving, he ends up here in a mounted-bandit den.”

The Human Butcher clicked his tongue.

“I don’t even feel like killing someone that old. Get rid of him.”

“Yes, sir.”

His subordinate was about to step forward when—

“Wait.”

The one who stopped him with an upraised hand was Black Sand. His brow furrowed as he stared at the old man.

*Something’s strange.*

The inn where they were staying had been built by mounted bandits. Its owner, cook, and servers were all either mounted bandits or former mounted bandits.

It was the only neutral ground in the Northern Gaoyuan, which was why it sometimes served as a place for gatherings and reconciliations like today’s.

*But he came crawling here on his own? And he’s that old?*

Anyone who set foot in the Northern Gaoyuan naturally knew the inn existed.

They also knew that an ordinary commoner who entered it would be as good as dead.

“What is it?”

“Shh. Wait a moment. Something about this doesn’t feel right.”

Black Sand’s reaction caused the others to sense the oddity as well.

“Come to think of it, how did he get here?”

“He looks like an outsider…”

“He’s not an outsider. There’s no way an old man like that could have reached this place with his body intact.”

Hundreds of mounted-bandit groups and nomadic tribes were scattered throughout the Northern Gaoyuan. Unless someone was exceptionally daring, they would never even consider crossing the plateau alone.

The four men, including Black Sand, fell into thought.

*Could he be…?*

*If he’s a martial artist, it’s possible.*

*A martial artist? That old man?*

*He’s bothering me. We should kill him.*

To the Human Butcher in particular, murder was no different from breathing. As he fearlessly reached for his sword sheath, Black Sand glared at him.

Then Sound Transmission slipped into the Human Butcher’s ear.

— I told you to wait. It won’t be too late to act after we observe him a little longer. Haven’t you ever heard that, in the Murim, you should be wary of women, children, and old men?

— You’re worrying over nothing. That sickly old man?

— Don’t act rashly. You never know what might happen in the Murim.

The old man looked as though he would die if someone merely poked him.

But the Human Butcher could not simply ignore Black Sand’s warning.

With an irritated sigh, he took his hand off his sword sheath.

— Good choice.

By then, the mysterious old man had reached the four men with trembling steps.

A strange tension hung in the air. The old man looked around with hazy eyes, then opened his mouth.

“W-Water…”

His voice was dry and parched as he searched for water. The people around him shook their heads with expressions that seemed to say, *Of course.*

But Black Sand was different. Careful and calculating by nature, he did not lower his guard until the very end.

“The elder seems thirsty. Bring him some cool water.”

“Yes, sir.”

After a mounted bandit handed him a cup, the old man gulped down the water as though his life depended on it. He drank so desperately that it seemed he might collapse.

Only after downing five or six cups in succession did the old man raise his head.

“Whew.”

“Feeling better now?”

A broad smile spread across the old man’s wrinkled face.

“Yes!”

“…”

“Thank you, mister!”

*Mister?*

Startled, Black Sand shot to his feet and grabbed the old man’s wrist.

There was no resistance. No strength at all. The thin bones looked as though they would snap if he applied even a little force.

“Elder?”

“Yes? Why?”

The old man’s smile and tone were like those of a child. Black Sand stared at him blankly, then his face twisted.

“Damn it. He’s senile.”

The tension drained out of him. He had definitely sensed something strange, but it seemed it had all been in his head.

With an important undertaking ahead of them, perhaps his nerves had simply been on edge.

Black Sand shook his head from side to side, and the Human Butcher laughed at him.

“They say you never know what will happen in the Murim. I suppose they were right. An old man suffering from age-related infirmities? Ha-ha-ha!”

“Shut your mouth.”

Black Sand answered curtly and began to release the old man’s wrist.

That was when—

“Where the hell is this?”

The voice was sharp and clear, completely different from before. The old man’s eyes had become focused as he looked around, then he let out a deep sigh.

“Damn it. You should die once you get old.”

It seemed he had finally returned to his senses. Laughter leaked out from various corners of the inn at his grumbling.

Black Sand had completely relaxed as well. He gave a quiet laugh and asked,

“Elder, are you feeling better now?”

The old man answered.

“Who told a little bastard like you that he could use *hao*-style speech with me? Are you from the Lower District Sect or something?”[^1]

[^1]: *Hao*-style speech is a semi-formal Korean speech level; its name sets up the pun on the Lower District Sect’s Korean name, *Haomun*.

“…”

“What are you holding my wrist for? You trying to get fresh with me?”

“W-Wait a moment.”

“Are you letting go or not? I’ll count to three. One, two, three.”

*Whoosh.*

Black Sand let go of the old man’s wrist before he even realized what he was doing. His mind was completely scrambled by the sudden turn of events.

*What the hell is this old man?*

The thick curses and rapid-fire words had made his body move on its own.

The old man was clearly nothing more than a deranged elderly man who did not know a single martial art, yet Black Sand felt as though he had been bewitched.

“Ha-ha-ha-ha! You got played beautifully!”

The Human Butcher burst into raucous laughter. He had already disliked Black Sand acting as leader when Black Sand was clearly a step below him in martial arts.

Seeing Black Sand humiliated by a senile old man made him feel thoroughly refreshed.

“That old man has quite a mouth on him. He made me laugh, so I suppose I’ll let him live.”

But the satisfied smile at the corner of the Human Butcher’s mouth did not last long.

A single sentence from the old man made it disappear.

“You worthless bastard… Don’t you have a mother and father?”

“…”

The inn fell into icy silence.

Who were Black Sand and the Human Butcher?

They were major figures who dominated the Northern Gaoyuan. Their forces were formidable, but each of them was also a Peak master capable of crushing an average mounted-bandit group with ease.

Yet the old man had carved the two men apart with only a few words.

“One’s a sodomite from the Lower District Sect, one grew up without parents and has only half a tongue, and the other two…”

The old man glanced at Temur and Chinggen, who wore their hair in queues, then sighed.

“Young men, and your foreheads are already completely bare. What a pity.”

No one had the energy to be surprised anymore. In the midst of the atmosphere thick with shock and horror, the old man clicked his tongue and noticed the food laid out in front of the four men.

“Well, damn, you’ve laid out one hell of a feast. I was hungry, too. What a stroke of luck.”

No one had time to stop him.

The old man grabbed a well-roasted duck by one leg and ripped into it.

“Wow, look how tender this meat is. It just melts on the tongue.”

*Crunch, crunch.*

After devouring both legs in the blink of an eye, the old man thrust a piece of meat toward the Human Butcher, who was trembling with rage and shock.

“You’re still young, so why are you trembling so much? Don’t waste away from weakness. Eat this. I hate dry breast meat—no, I can’t eat it. My teeth aren’t very good.”

*Crack.*

Everyone in the inn heard the same sound.

It was the sound of the last thread of the Human Butcher’s reason snapping—and the death knell of a man.

“You goddamn old bastard!”

The next moment, the Human Butcher, beside himself with rage, shot upward like lightning. At the same time, crimson Sword Energy poured from the horse-chopping sword in his hand and swept across everything in front of him.

“What the hell!”

“Get out of the way!”

*Kaboom!*

Temur and Chinggen had barely thrown themselves aside when a thunderous explosion rang out.

Hundreds, even thousands, of wooden fragments flew in every direction as a cloud of dust billowed through the air.

“Die! Die! Die!”

The people watching the scene felt the hair rise on the backs of their necks. Judging by the madness radiating from the Human Butcher, there was no doubt the old man had died without leaving behind even a single scrap of flesh.

“How dare a senile old man—! Aaaaargh!”

*Boom! Boom! Boom!*

A relentless storm of Sword Energy continued to pour forth. The Human Butcher finally withdrew his horse-chopping sword after roughly a quarter of an hour.

“Huff… huff…”

Breathing heavily, he swung his sword through the air. The resulting sword pressure scattered the dust cloud, revealing a half-pulverized ruin.

As everyone had expected, the old man was nowhere to be seen.

“He was the bravest person I’ve ever seen.”

“Farewell, elder.”

“Why did he have to provoke the Human Butcher…?”

“As expected of those Han Chinese. They’re unbelievably savage.”

The more than two hundred mounted bandits and nomads were whispering among themselves when—

*Crunch, crunch. Gulp. Guh-hup!*

“…”

“…”

“…”

At first, they were simply dumbfounded.

In an atmosphere like this, what kind of clueless idiot was eating food and drinking liquor?

But it took no more than an instant for their confusion to become astonishment, and their astonishment to become horror.

“T-The old man! The old man is alive!”

“What? Where?”

“Behind us! I heard him behind us!”

Someone shouted.

Then a sharp, clear voice followed, making everyone doubt their own ears.

“Young people these days are a real problem. So rude. Is my name *old man*? Am I your friend?”

“W-Whoa!”

“That does it. I’ll teach you lot some manners today.”

*Thud-thud-thud! Whoosh!*

The mounted bandits and nomads filling the inn went flying through the air one after another.

Their limbs were mangled and their faces smashed as they were flung away. The sight made the leaders break into cold sweats.

*W-What is this?*

*How is he over there?*

*I didn’t even see him move.*

A master.

A master capable of deceiving the eyes of even Peak masters like themselves.

Black Sand, Temur, and Chinggen had gone rigid when, as the only exception, one man charged straight toward the old man.

“You goddamn old bastard!”

The Human Butcher was already beyond reason and had no reservations left.

The old man saw him rushing forward and frowned.

“You…”

“That’s right, it’s me! This time, I’ll definitely kill you!”

“So you’re the one without parents.”

“Graaaargh!”

*Whoooosh!*

*Mount Tai Presses Down on the Crown.*

At that moment, the horse-chopping blade, its crimson Sword Energy blazing, was about to split the crown of the old man’s head.

The old man swung something.

*Slice! Thud!*

It felt as though time had stopped.

In the silence, not even a breath could be heard. Everyone doubted their own eyes.

The horse-chopping sword had been cut in half.

And in the old man’s hand was a tiny object.

“T-That’s…”

For the first time, the Human Butcher’s eyes regained their composure. He stared at the old man in fear and astonishment.

“…A chicken bone?”

“There’s no part of a chicken that goes to waste. The meat is delicious, the bones make a fine broth when simmered down, and sometimes they’re even good for wielding Sword Energy.”

He had used a chicken bone to wield Sword Energy.

The Human Butcher had never seen or heard of anything so bizarre.

He understood instinctively.

*A master. A Supreme Peak master. Someone I could never oppose.*

The old man looked at the Human Butcher, who had fallen into shock, and muttered,

“Come to think of it… You’re a vicious one. The smell of blood is coming off your entire body.”

Every word sent a chill through him. He had lived his entire life as a predator, yet now he was no more than a rat before a tiger.

“You can’t just leave someone like this alive…”

The Human Butcher suddenly felt a chill. The deadly aura flowing from the old man’s entire body made his teeth chatter.

“P-Please.”

“Hm?”

“Please spare me. Please…”

Tears ran down his cheeks. His trousers grew damp, and the horse-chopping sword slipped from his limp hand.

The plea of a butcher who had spent his entire life taking other people’s lives was an unbelievable sight.

The old man looked at him for a moment before speaking.

“Don’t be afraid.”

*I’m safe. I’m alive! I escaped death!*

The Human Butcher let out a relieved sigh without realizing it.

That was when—

*Thump.*

A hand with protruding knuckles pressed against his chest. The old man’s hand was rough and wrinkled.

And that was the end.

“…Huh?”

The world turned upside down along with his faint question. Blood poured from the seven orifices of his fallen body and soaked the floor.

*He said he would spare me. Why?*

Beyond his fading vision and the sounds receding into the distance, he heard the old man’s voice.

“Don’t be afraid. I’ll send you off without pain.”

The old man was telling the truth.

There was no pain.

* * *

The Human Butcher.

A Peak master whose evil reputation had spread all the way to the Central Plains had died from a single move.

“Well, then…”

The old man addressed the people who had frozen in place.

“Where is this place?”
```
