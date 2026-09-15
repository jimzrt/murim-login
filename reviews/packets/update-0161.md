<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0161.txt",
      "sha256": "7408bb420c0d0222ca8eb31b9670e30e42eae6e9667ca793bff8762ca67d7dc6",
      "bytes": 13758
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2a2e688ae05c71cd5fcfef1c1e94deb4d452f29f2c325c1a60367c4223df9024",
      "bytes": 7964
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bbf03926ac60b8ee16cf530eebe9f8db9affab4766278c33944e04020e9fbeb2",
      "bytes": 39256
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "5998ae95e091722f9af52b9ce65ade1b7b398b185338bb3237dd4fd6f779d2ef",
      "bytes": 512
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "b4dcb737e0f932c4ee68d2bc35f04b6b089bc1059c8cca18c21fc25c32385030",
      "bytes": 520
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "08fb5e2862aa0633dea5badc5f161b7c7e46a1594814695606cd3adcbc1e53f3",
      "bytes": 1356
    },
    {
      "path": "characters/Temur.md",
      "sha256": "7e88fa446cf564c38ef6b275508cfe3e86eae28f3397629f3da086d7baa24fc0",
      "bytes": 514
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "ba87558f45276ad4d311176b4a99cdfc039f24a16e7e7e006c9dde9bfee8e002",
      "bytes": 4621
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5dfdd8a2467a16a4ad98880e7e80b89470356ee12af3de28fdb86de1ca7ae634",
      "bytes": 30778
    }
  ],
  "estimated_tokens": 28737
}
-->

# Durable State Update — Chapter 161

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 161. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 161. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 161,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 161,
    "continuity_sources": [161],
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
    "Temur and Chinggen are Northern Gaoyuan chieftains who each command one hundred tribespeople; the Human Butcher is a mysterious Han Chinese mounted-bandit power who commands fifty subordinates and intimidates Temur at a gathering of four regional powers."
  ],
  "continuity_sources": [
    160
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him, and did he actually go to the Jin Family after breaking seclusion to find Cheongpung?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?",
    "Who is the unnamed middle-aged man at the Northern Gaoyuan gathering, and what purpose does the gathering serve?"
  ],
  "safe_through": 160,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally; render 초일류 as “advanced First Rate,” 군문 as “military,” 풍운검군 as “Wind-and-Cloud Sword Lord,” and 오촌 당숙 as “father's cousin.”",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” 광염 as “light-flames,” 검명 as “Sword Cry,” and 창명 as “Spear Cry.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” 환골탈태 as “Bone Transformation,” and 전음 as “Sound Transmission.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 태초 마을 as “Taecho Village,” 벽호공 as “Wall Lizard Technique,” 낙안봉 as “Falling Goose Peak,” 대초원 as “Great Steppe,” 마유주 as “mare's-milk wine,” 게르 as “ger,” and 북부 고원 as “Northern Gaoyuan.”",
    "Render 황하방 as “Yellow River Gang,” 소공문 as “Sogong Sect,” 남부상회 as “Southern Merchant Guild,” 내당주 as “Inner Hall Master,” 내외당 as “Inner and Outer Halls,” 세가 as “great family,” and 한족 as “Han Chinese.”",
    "Render 암향표 as “Dark Fragrance Drift,” 복호권 as “Crouching Tiger Fist,” 천근추 as “Thousand-Catty Drop,” 야성 as “Wildness,” 오행매화보 as “Five-Element Plum Blossom Steps,” 공수납백인 as “Empty-Hand Seizes the Blade,” 매화오품지 as “Plum Blossom Five-Point Finger,” 벽을 넘어서 as “Beyond the Wall,” and 절정 고수 as “Peak Master.”",
    "Retain Taekyung's instant-noodle flavor joke with “mild Neoguri,” “Jin Ramen spicy flavor,” and “Puramyeon spicy flavor”; render 천근거력 as “the force to move a thousand catties,” 인도 as “Human Butcher,” 대칸 as “Great Khan,” 텡게르 as “Tengger,” and preserve the 무공/무공 wordplay as “martial arts” and “empty space.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 위팽     | **Wipeng**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 살기     | **killing intent**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 160
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his fellow chieftain, and Chinggen repeatedly restrains Temur's recklessness

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 160
- **Aliases:** None
- **Role:** Mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering and intimidates Temur

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 148
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 160
- **Aliases:** None
- **Role:** Northern Gaoyuan chieftain commanding one hundred tribespeople and claiming descent from the khans
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and hostile to Han Chinese encroachment
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his fellow chieftain and restrains him from provoking the Human Butcher

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 155
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung

## Korean source

```text
＃161화



“말귀가 어두운 친구로군.”

사내, 인도(人屠)의 말에 테무르는 간담이 서늘해졌다. 담담한 목소리 속, 비수처럼 도사린 살기를 느꼈기 때문이다.

‘인간 백정이라더니, 무슨 놈의 살기가…….’

그러나 이렇게 물러날 수는 없었다.

이 자리를 위해 데리고 온 부족원들, 그리고 한족 출신의 마적들이 그의 행동 하나하나를 주시하고 있었다.

‘빌어먹을.’

부족장으로서의 명예와 한 줄기 남은 이성이 충돌했다.

검을 뽑을 것인가, 말 것인가. 갈등하는 테무르를 구해 준 것은 다음 순간 들려온 웃음소리였다.

“하하하! 역시 천하의 호걸들이시오. 나처럼 담 작은 소인배는 무서워서 끼어들 수도 없겠어.”

테무르가 웃음소리의 주인을 바라봤다.

“당신은 누구요?”

“나 말이오?”

반백의 중년인이 푸근하게 웃었다.

한쪽 눈에 안대를 두르지만 않았더라면 마음씨 좋은 상인처럼 보일 만큼 온순한 인상이었다.

“내 이름은 두 개인데, 하나는 고향을 떠나며 버렸고 다른 하나는 초원에서 만난 벗들이 만들어 주었지. 그중 뭐가 궁금하오?”

테무르는 대답하지 않아도 되었다. 인도가 그의 정체를 대신 입에 담았기 때문이다.

“흑사(黑砂), 시답잖은 잡설은 적당히 하지.”

“어이쿠. 이렇게 까발리는 게 어디 있소? 한창 재밌어지던 참인데.”

“하나도 재미없다.”

“그러니 당신이 백정 소리를 듣는 거요. 쯧쯧.”

과장되게 혀를 차는 중년인의 정체를 깨달은 테무르와 칭겐이 눈을 크게 떴다.

“흑사? 흑사대?”

“당신이 바로 그?”

안대를 쓴 중년인, 흑사가 시원스럽게 고개를 끄덕였다.

“맞소, 내가 흑사요.”

“……!”

“……!”

흑사대. 오직 한족으로만 이루어진 그들은 거친 초원에서도 손꼽히는 강자들이다.

숫자는 고작 일백이지만 하나하나가 마상무예의 달인이며 뛰어난 무공의 소유자인 것으로 알려진.

바로 그 흑사대의 수괴가 이처럼 경박한 사내였다니.

칭겐은 혀를 내둘렀다.

‘그래서 저 포악한 인도가 백정 소리를 듣고도 별 반응이 없던 거였군.’

그야말로 흑사였기에 가능했던 일이다. 다른 사람이었다면 인도에 의해 진작 혀가 뽑히고 목이 잘려 나갔을 것이다.

한데…….

“당신이 왜 여기에 있는 거요?”

놀라움을 가라앉힌 테무르도 칭겐의 질문에 의구심 어린 눈빛을 던졌다.

“그에 관해서는 나도 물어보고 싶군.”

노골적인 경계심에 흑사가 빙긋 웃었다.

“혹 서신을 한 통 받지 않았소?”

테무르와 칭겐이 동시에 흠칫했다.

“서신?”

“어떻게 그 사실을?”

“내가 바로 그 서신을 보낸 사람이니까.”

“그럴 리가. 분명 서신에는 천풍단주의 인이 찍혀 있었는데.”

어리둥절해하는 테무르와는 달리, 어느 정도 상황 파악을 끝낸 칭겐은 침잠한 눈빛으로 흑사를 바라봤다.

“천풍단주와는 어떤 관계요? 그는 지금 어디 있소?”

“당신이 칭겐이로군. 젊은 족장답지 않게 침착하고 눈치가 빠르다는 말은 들었소.”

“내가 원하는 대답이 아니오.”

“눈빛이 매섭구먼. 이래서야 무서워서 말이나 꺼낼 수 있겠나. 그래도 뭐, 이 자리에 온 이상 감출 비밀도 아니니 알려 드리리다.”

넉살을 떨던 흑사가 말을 이었다.

“천풍단주는 내 명령에 따라 대동 인근을 배회하며 시선을 끌고 있소.”

명령.

그것이 의미하는 바는 명백했다.

‘지금까지 감쪽같이 속았군.’

천풍단주는 흑사의 수하가 분명하다. 머릿수가 물경 오백에 이르는 천풍단도 흑사대의 하부조직에 지나지 않는다는 뜻이다.

테무르와 칭겐은 말없이 눈빛만 주고받았다.

‘흑사대로도 충분히 강한데 천풍단까지 더하면……?’

‘초원의 판도를 바꾸기에 부족함이 없지.’

그런 그들을 바라보는 흑사의 입가에 진한 웃음이 맺혔다.

“생각이 많으신가 보군.”

“솔직히 당황스러운 것은 사실이오.”

“도대체 당신의 꿍꿍이가 뭐요?”

“꿍꿍이는 무슨. 서로에게 득이 되는 거래를 하자는 것뿐이오. 서신을 읽었다면 알 텐데?”

테무르와 칭겐. 두 사람은 보름 전 받았던 서신의 내용을 떠올렸다.

화살촉에 묶여 날아온 서신에는 짤막한 한 줄이 적혀 있었다.



칸이 되고 싶다면 오시오.



칸! 초원의 지배자, 수많은 전사를 거느린 위대한 왕.

생각만으로도 피가 끓어오르는 단어다. 일족의 부흥을 꿈꾸는 젊고 강한 두 부족장에게는 더더욱 그랬다.

“작금의 초원은 사분오열됐소. 과거 그대들의 선조가 세운 찬란한 대제국을 생각하면 믿기 힘들 정도지.”

흑사는 마유주를 저으며 말을 이었다.

“나를 도와준다면 나도 그대들을 돕겠소. 병장기와 말, 재물. 필요하다면 수하들도 보내 주지. 조각난 초원을 규합하시오. 적들을 무릎 꿇리고 절대적인 복종을 약속받으시오. 장담컨대 십 년 안에 대초원의 칸이 될 수 있을 거요.”

“말은 쉽군.”

빈정거리는 듯한 테무르와는 달리 칭겐은 침착했다.

“왜 하필 우리요?”

“젊고 유능하며, 야심이 넘치니까. 칸의 핏줄을 이었다는 정통성도 한몫했고. 어쨌든 내 제의는 간단하오.”

흑사는 점차 사그라지는 불길 속으로 딱딱하게 굳은 말똥을 밀어 넣었다. 순간 솟구친 불길이 그의 눈동자 속에서 일렁였다.

“나와 함께 성(城)을 도모해 보지 않겠소?”



* * *



“성? 산서를 말하는 거요?”

“그럼 어디겠소?”

두 부족장은 그제야 그의 속내를 대충 감 잡았다. 항산검문이 무너진 공백을 비집고 들어가려는 술수다.

문제는 칸이니, 지원이니 하며 거창한 포부를 운운한 것 치고는 그들에게 딱히 매력적인 제안이 아니라는 것이었다.

“다들 표정이 영 아니군.”

칭겐이 탐탁지 않은 얼굴로 대답했다.

“무주공산이 된 북부를 털어 보겠다는 생각이라면 아무래도 어렵지 않겠소?”

“어째서?”

“태원진가가 발 빠르게 움직이고 있으니까. 북부 전역에 지부를 세우는 한편, 관에서도 나서고 있다고 들었소.”

그들에게도 정해진 선이라는 것이 있다.

상단을 습격하면 마적이지만 성을 침범해 양민들을 약탈하면 반란군이 된다.

반란을 진압하기 위해 수만 명의 토벌군이 파견되기라도 한다면 대적할 방법이 없다.

“고향에서까지 쫓겨나고 싶지는 않소. 풍양처럼 개죽음당하기도 싫고.”

칭겐의 말에 테무르도 고개를 끄덕였다. 호전적인 성격의 그였지만 현실은 인정해야 했다.

“심지어 풍양 그놈은 관은 건드리지도 않았지. 태원진가의 어린놈들한테 죽었어.”

“풍양의 수하들은 사백에 달했소. 그중 살아 돌아온 자들이 십 분지 일도 안 되오.”

그때, 가만히 대화를 듣고 있던 인도가 불쑥 입을 열었다.

“풍양은 초원에서 도망친 놈이다. 밑에 있던 놈들도 급하게 끌어모은 떨거지들에 불과했고.”

“풍양을 본 적이 있소?”

“두어 번. 별거 없는 놈이었지. 단언컨대 이 자리에 모인 이들 중, 놈보다 약한 자는 없다. 아, 물론 저 얼간이도 포함해서.”

“이 새끼가!”

“목소리를 낮춰라. 목젖을 도려내 버리기 전에.”

“한족 놈이 입만 살았군. 할 수 있을 것 같나?”

“물론. 지금 당장이라도.”

스르릉.

두 사람의 허리춤에서 도신이 모습을 드러낸 그때였다.

“거 참. 적당히들 하시오.”

연배로나, 세력으로나 흑사를 무시할 사람은 아무도 없다.

팽팽한 기 싸움 끝에 두 사람이 동시에 병장기를 집어넣자 흑사가 재밌다는 듯이 웃으며 칭겐에게 말했다.

“관은 걱정할 것 없소. 태원진가와 우리 사이의 문제로 끝날 테니까.”

“그게 무슨 소리요?”

“누구도 반응 못 할 만큼 벼락처럼 해치우면 되지 않겠소?”

“그게 될 것 같소? 산서성은 이미 태원진가의 손에 들어간 것이나 마찬가지요. 대동을 돌파한다고 쳐도 그때쯤이면 태원진가의 본대와 수많은 중소문파들이 기다리고 있을 테고.”

“모이기 전에 친다면 어떻겠소? 그것도 머리만 골라서.”

“……뭐?”

“사흘 후, 다가오는 원단에 산서성 모든 문파의 수뇌부들이 태원진가로 집결할 거요. 우린 대동이 아니라 하곡(河曲)을 통해 진입. 그대로 태원을 향해 돌격하는 거지.”

“……!”

“무장을 최소화하고 지구력이 뛰어난 초원마를 확보한다면 하루에 오백 리는 너끈하지. 짧으면 이틀, 길면 사흘 만에 적들을 칠 수 있소.”

산서성의 절반을 가로질러 상대의 머리를 친다니.

실로 담대하고도 무모한 계획에 칭겐의 목소리가 떨렸다.

“자, 잠깐. 놈들이 미리 알아차리고 방비한다면?”

“방비라…… 정확히 어떤 상황을 말하는 거요?”

“말했다시피 북부에는 태원진가의 지부가 속속 들어서고 있소. 일일이 전투를 치르면서 전진하면 기동력이 떨어지고, 무시하고 지나친다면 우리가 들이닥치기도 전에 소식을 알게 되겠지.”

“그 부분은 걱정 마시오. 우리는 단 하나, 하곡 지부만 박살 내면 되니.”

“하면 다른 지부들은?”

“그때쯤이면 놈들은 대동에서 피 터지게 싸우고 있을 거요.”

“대동…… 아. 설마!”

“천풍단주가 제 몫을 톡톡히 할 거요. 그 날만큼은 사정없이 날뛰라고 일러두었거든.”

천풍단은 누구나 아는 북부 고원의 강자.

머릿수도, 개개인의 실력도 적풍단 때보다 더했으면 더했지, 덜하진 않을 것이다.

“반나절이면 북부에 존재하는 태원진가의 지부들이 텅텅 빌 거요. 급한 불이 났는데 뒤를 돌아볼 겨를이 있겠소?”

흑사의 말 그대로다. 지부는 천풍단을 막기 위해서 무인들을 박박 긁어모아 대동으로 보낼 것이고, 그 틈을 타 진짜 본대가 하곡을 넘어 남하한다.

막아서는 모든 것들을 말발굽으로 짓밟으며…….

“또 현재 태원진가는 북부 안정에 전력을 기울이고 있소. 내 알아본 바로는 본가의 무인들은 일백이 될까 말까지.”

흑사의 목소리가 이어졌다.

“산서성 모든 문파가 참석하는 자리요. 아무리 태원진가가 크다 한들 그들 모두를 먹이고 재울 수는 없는 법. 본가에 남아 있는 무인까지 다 합쳐 봐야 이백이나 될까?”

칭겐은 목이 바짝바짝 탔다. 이 자리에 모인 이들의 휘하 병력만 합쳐도 삼백 명은 우습다.

아니, 밑바닥까지 긁어모은다면 그 두 배까지도 가능하다.

‘고수들끼리의 싸움도 밀리지 않는다.’

흑사. 인도. 테무르와 칭겐.

이 자리에 모인 넷은 하나같이 뛰어난 절정 고수들이다.

죽은 풍양을 직접 만난 적이 있다는 인도의 말에 따르면 이 중 풍양보다 무공이 떨어지는 아무도 없다.

‘하지만 태원진가의 진천검과 산서잠룡은 합공한 끝에 겨우 풍양을 쓰러트렸다.’

이미 사실로 확인된 이야기다.

풍양이 노강호로 불리는 항산호마저 쓰러트린 덕분에 항간에는 북부 고원의 마적들이 웬만한 일류 무림인보다 강하다는 소문마저 돌고 있었다.

‘이거 어쩌면…….’

조용히 생각에 잠긴 칭겐을 흑사가 웃음기 띤 눈빛으로 응시했다.

“어떻소?”

침을 꼴깍거리며 듣고 있던 테무르가 외쳤다.

“젠장. 그런 끝내주는 계획을 들려주고 물어보면 어떡하라고? 무조건 하겠소!”

“나도 응하겠소.”

마침내 생각을 끝마친 칭겐도 승낙하자, 인도가 흉흉한 웃음을 머금으며 끼어들었다.

“난 다른 건 다 필요 없어. 귀검(鬼劍) 위팽. 그놈만 내 몫으로 남겨 주면.”

“물론이지. 내 약속함세.”

만면에 미소를 가득 띤 흑사가 세 사람을 둘러보며 말했다.

이 제안이 받아들여진 이상, 그는 암묵적인 좌장(座長)이 된 것이나 마찬가지였다.

“이번 일로 얻는 모든 것들은 정확히 사 등분. 만약 이를 어기는 자가 있다면 천하 끝까지라도 쫓아가서 목을 벨 걸세. 이의 있나?”

“없소.”

“나도.”

“서신에 적은 약속은 지키시오.”

“물론.”

시원하게 대답한 흑사가 빈 사발에 마유주를 가득 따라 돌렸다.

“자, 결의를 맺었으니 오늘은 흠뻑 취하세!”

“우와아아!”

“마시자! 술 더 갖고 와!”

유쾌한 함성이 객잔 곳곳에서 터져 나왔다.

모두 마유주만큼이나 후끈 달아오른 분위기 속에서 잔을 기울이던 그때였다.

끼이이이익.

시끌벅적한 소음 사이, 객잔의 문이 열리고 한 사람이 모습을 드러냈다.
```

## Final English reading copy

```markdown
# Chapter 161

“You’re a slow one, friend.”

The Human Butcher’s words sent a chill through Temur. He could feel the killing intent lurking in the man’s calm voice like a dagger.

*They call him the Human Butcher, but what the hell kind of killing intent is that…?*

But he could not back down here.

The tribespeople he had brought for this gathering, along with the Han Chinese mounted bandits, were watching his every move.

*Damn it.*

The honor he carried as a chieftain clashed with the last shred of reason in his mind.

Should he draw his saber or not? As Temur wavered, a burst of laughter came to his rescue.

“Ha-ha-ha! As expected of the heroes of the world. A timid little man like me is too frightened to get involved.”

Temur looked toward the source of the laughter.

“Who are you?”

“Me?”

The middle-aged man, whose hair was half gray, smiled warmly.

If not for the eyepatch covering one eye, he would have looked as gentle as a kindhearted merchant.

“I have two names. I abandoned one when I left my homeland, while the other was given to me by friends I met on the steppe. Which one are you curious about?”

Temur did not need to answer. The Human Butcher revealed the man’s identity for him.

“Black Sand. Enough with the pointless drivel.”

“Oh, come on. What kind of person exposes someone like that? I was just getting to the fun part.”

“It wasn’t fun at all.”

“That’s why people call you the Butcher. Tsk, tsk.”

Temur and Chinggen realized who the middle-aged man was and opened their eyes wide.

“Black Sand? The Black Sand Band?”

“You’re that man?”

The eyepatched middle-aged man, Black Sand, nodded without hesitation.

“That’s right. I’m Black Sand.”

“…”

“…”

The Black Sand Band. Composed exclusively of Han Chinese, they were counted among the strongest powers on the harsh steppe.

There were only a hundred of them, but every single one was said to be a master of mounted combat and a martial artist of exceptional skill.

To think the leader of the Black Sand Band was such a frivolous man.

Chinggen was astounded.

*So that’s why that vicious Human Butcher didn’t react when he was called a butcher.*

It was only possible because the man was Black Sand. If anyone else had said it, the Human Butcher would have pulled out his tongue and cut off his head long ago.

But…

“Why are you here?”

Once his surprise had subsided, Temur also looked at Black Sand suspiciously.

“I’d like to ask you the same thing.”

Black Sand smiled faintly at their open wariness.

“Didn’t you receive a letter?”

Temur and Chinggen both flinched.

“A letter?”

“How did you know about that?”

“Because I’m the one who sent it.”

“That’s impossible. The letter clearly bore the seal of the Heavenly Wind Band Leader.”

Unlike Temur, who was bewildered, Chinggen seemed to have figured out the situation to some extent. He regarded Black Sand with a grave, thoughtful gaze.

“What is your relationship with the Heavenly Wind Band Leader? Where is he now?”

“So you’re Chinggen. I’ve heard you’re calm and sharp for a young chieftain.”

“That isn’t the answer I want.”

“You have a frightening look in your eyes. How am I supposed to say anything with you staring at me like that? Still, now that you’re here, there’s no secret worth hiding. I’ll tell you.”

After joking around, Black Sand continued.

“The Heavenly Wind Band Leader has been wandering around near Datong under my orders, drawing attention.”

*Under his orders.*

The meaning was obvious.

*We’ve been completely fooled all this time.*

The Heavenly Wind Band Leader was clearly Black Sand’s subordinate. That meant the Heavenly Wind Band, which numbered a full five hundred, was nothing more than a subsidiary organization of the Black Sand Band.

Temur and Chinggen exchanged silent glances.

*The Black Sand Band is already strong enough. And if you add the Heavenly Wind Band…?*

*It would be more than enough to change the balance of power on the steppe.*

A deep smile spread across Black Sand’s lips as he watched them.

“You seem to have a lot on your minds.”

“To be honest, this is rather bewildering.”

“What exactly are you scheming?”

“Scheming? I’m simply proposing a deal that benefits us all. You would know if you read the letter.”

Temur and Chinggen recalled the contents of the letter they had received fifteen days earlier.

The letter, tied to an arrow and shot to them, contained one short line.



*If you want to become a khan, come.*



A khan! The ruler of the steppe, a great king commanding countless warriors.

The very word made their blood boil. It was even more powerful to two young and strong chieftains who dreamed of restoring their clans to glory.

“The steppe is fractured into pieces these days. It’s hard to believe when you think of the glorious great empire founded by your ancestors.”

Black Sand swirled his mare’s-milk wine as he continued.

“If you help me, I’ll help you in return. Weapons, horses, wealth. If necessary, I’ll even send you some of my subordinates. Unite the fragmented steppe. Bring your enemies to their knees and force them to swear absolute obedience. I guarantee that you can become the khan of the Great Steppe within ten years.”

“Easy for you to say.”

Unlike the sarcastic Temur, Chinggen remained calm.

“Why us?”

“Because you’re young, capable, and ambitious. Your legitimacy as descendants of the khans also helps. In any case, my proposal is simple.”

Black Sand pushed a hard, dried lump of horse dung into the fire, which was gradually dying down. The flames suddenly leaped up and flickered in his eyes.

“Would you care to seize a city with me?”



* * *

“A stronghold? You mean Shanxi?”

“Where else would I mean?”

Only then did the two chieftains roughly grasp his intentions. He intended to force his way into the power vacuum left by the collapse of the Mount Heng Sword Sect.

The problem was that, for all his grand talk of khans and support, his proposal offered them little that was actually attractive.

“None of you look very pleased.”

Chinggen answered with an unconvinced expression.

“If you’re thinking of raiding the north now that it’s become ownerless, wouldn’t that be difficult?”

“Why?”

“Because the Jin Family of Taiyuan is moving quickly. I’ve heard they’re establishing branches throughout the north, while the government is also getting involved.”

Even they had a line they could not cross.

Attacking a merchant caravan made them mounted bandits, but invading a city and plundering civilians would make them rebels.

If an army of tens of thousands were dispatched to suppress the rebellion, they would have no way to oppose it.

“I don’t want to be driven out of my homeland, either. And I have no desire to die a dog’s death like Pung Yang.”

Temur nodded at Chinggen’s words. He was hot-tempered, but he had to acknowledge reality.

“That bastard Pung Yang didn’t even touch the government. He was killed by the young brats from the Jin Family of Taiyuan.”

“Pung Yang had nearly four hundred subordinates. Less than one in ten of them made it back alive.”

The Human Butcher, who had been listening silently, suddenly spoke.

“Pung Yang was a man who fled from the steppe. The people under him were nothing more than a bunch of ragtag strays he hastily gathered.”

“You’ve met Pung Yang?”

“Once or twice. He was nothing special. I can say this with certainty: no one here is weaker than him. Ah, that includes that idiot, of course.”

“You bastard!”

“Lower your voice before I cut out your Adam’s apple.”

“The Han Chinese bastard has a big mouth. You think you can do it?”

“Of course. Right now, if you want.”

*Schriing.*

Just as the blades at both men’s waists slid from their sheaths—

“Honestly. Keep it under control.”

There was no one here who could disregard Black Sand, whether because of his age or his power.

After the two men exchanged a tense battle of wills and sheathed their weapons at the same time, Black Sand laughed as though he found it amusing and spoke to Chinggen.

“You don’t need to worry about the government. This will end as a matter between the Jin Family of Taiyuan and us.”

“What do you mean?”

“If we finish the job like a bolt of lightning before anyone can react, what could they do?”

“Do you think that’s possible? Shanxi Province is practically already in the hands of the Jin Family of Taiyuan. Even if we break through Datong, the family’s main force and countless small and medium-sized sects will be waiting by then.”

“What if we strike before they gather? And target only their heads?”

“…”

“What?”

“In three days, on the coming New Year’s Day, the heads of every sect in Shanxi Province will gather at the Jin Family of Taiyuan. We’ll enter through Hequ instead of Datong, then charge straight toward Taiyuan.”

“…”

“If we keep our weapons to a minimum and secure hardy steppe horses with excellent endurance, we can easily cover five hundred li in a day.[^1] We can strike the enemy in as little as two days, or three at the most.”

Crossing half of Shanxi Province to strike directly at the enemy’s head.

It was such a bold and reckless plan that Chinggen’s voice trembled.

“W-Wait. What if they realize what we’re doing in advance and prepare?”

“Prepare? What exactly do you mean?”

“As I said, branches of the Jin Family of Taiyuan are being established throughout the north. If we advance while fighting our way through each one, we’ll lose our mobility. If we ignore them and pass by, they’ll hear about us before we even arrive.”

“Don’t worry about that. We only need to smash the Hequ branch.”

“Then what about the other branches?”

“By then, they’ll be fighting for their lives in Datong.”

“Datong… Ah. Could it be?”

“The Heavenly Wind Band Leader will do his part. I told him to run wild without restraint on that day.”

The Heavenly Wind Band was a northern plateau power everyone knew.

Their numbers and the individual skill of their members were at least equal to those of the Red Wind Band, if not greater.

“In half a day, the Jin Family of Taiyuan’s branches throughout the north will be empty. With a fire burning in front of them, do you think they’ll have time to look behind them?”

Black Sand’s words were exactly right. The branches would scrape together every martial artist they had and send them to Datong to stop the Heavenly Wind Band. Taking advantage of that opening, the real main force would cross Hequ and advance south.

Trampling everything in their way beneath their horses’ hooves…

“Also, the Jin Family of Taiyuan is currently devoting all its strength to stabilizing the north. From what I’ve learned, there might not even be a hundred martial artists in the main family.”

Black Sand’s voice continued.

“This is a gathering attended by every sect in Shanxi Province. No matter how large the Jin Family of Taiyuan is, it can’t feed and house all of them. Even if you add every martial artist remaining at the main family, there may be only two hundred.”

Chinggen’s throat went dry. The forces under the people gathered here alone totaled three hundred without difficulty.

No, if they scraped together every last person, they could double that number.

*We won’t be outmatched even in a battle between masters.*

Black Sand. The Human Butcher. Temur and Chinggen.

All four of the people gathered here were exceptional Peak masters.

According to the Human Butcher, who had personally met the dead Pung Yang, no one here had inferior martial arts to him.

*But the Heaven Shaking Sword and the Sleeping Dragon of Shanxi from the Jin Family of Taiyuan only barely defeated Pung Yang after joining forces.*

That had already been confirmed as fact.

Pung Yang had even defeated the Tiger of Mount Heng, a veteran of the martial world. As a result, rumors had spread that the mounted bandits of the northern plateau were stronger than most First Rate martial artists.

*Could this actually be…?*

Black Sand watched Chinggen, who had fallen silent in thought, with amusement in his eyes.

“What do you think?”

Temur, who had been listening while repeatedly swallowing, shouted.

“Damn it! How can you tell me about such a fantastic plan and then ask what I think? I’m in, no matter what!”

“I’ll accept as well.”

Chinggen finally finished thinking and agreed. The Human Butcher cut in with a vicious smile.

“I don’t need anything else. Just leave Ghost Sword Wipeng to me.”

“Of course. You have my word.”

Black Sand, his face filled with a broad smile, looked around at the three men.

Now that they had accepted his proposal, he was effectively their presiding leader.

“Everything we gain from this will be divided into four equal shares. If anyone breaks that agreement, I’ll chase them to the ends of the world and cut off their head. Any objections?”

“None.”

“Me neither.”

“Keep the promise written in the letter.”

“Of course.”

Black Sand answered readily and filled an empty bowl with mare’s-milk wine before passing it around.

“Now that we’ve sealed our resolve, let’s get thoroughly drunk today!”

“Waaaaah!”

“Let’s drink! Bring more alcohol!”

Cheerful shouts erupted from every corner of the inn.

And just as they were raising their bowls in an atmosphere as heated as the mare’s-milk wine itself—

*Creeeeak.*

Amid the uproar, the inn’s door opened, and someone stepped inside.

[^1]: A *li* is a traditional Chinese unit of distance.
```
